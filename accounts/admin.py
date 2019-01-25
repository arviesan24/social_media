from django.contrib import admin
from accounts.models import Profile
from accounts.models import Relationship
from accounts.models import Request
from accounts.models import User

from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm


admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Request)
admin.site.register(User, UserAdmin)
