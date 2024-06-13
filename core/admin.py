from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import core.models as core

admin.site.register(core.usuarios, UserAdmin)