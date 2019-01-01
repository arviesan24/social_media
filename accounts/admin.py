from django.contrib import admin
from accounts.models import Relationship
from accounts.models import Request
from accounts.models import User

from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm


admin.site.register(Relationship)
admin.site.register(Request)
admin.site.register(User)
