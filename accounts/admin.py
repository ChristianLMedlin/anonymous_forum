from django.contrib import admin

from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password", "email_address", "creation_date",
            "last_active_date")

admin.site.register(User, UserAdmin)