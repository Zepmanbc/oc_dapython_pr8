from django.contrib import admin

# Register your models here.

from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    fields = ('email', 'first_name', 'last_name')
    readonly_fields = ['email']
    list_display = ('email', 'first_name', 'last_name', 'last_login',)
