from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Identity, Person

admin.site.register(Identity, UserAdmin)
admin.site.register(Person)
