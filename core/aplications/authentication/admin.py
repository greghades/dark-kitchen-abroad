from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser,CodesVerification

# Register your models here.
class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ('id', "name", "last_name", "email")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CodesVerification)
admin.site.unregister(Group)