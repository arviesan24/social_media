from django.contrib import admin
from accounts.models import Relationship
from accounts.models import Request
from accounts.models import User


admin.site.register(Relationship)
admin.site.register(Request)
admin.site.register(User)
