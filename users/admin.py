from django.contrib import admin

# Register your models here.
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')
    filter_horizontal = ['groups', 'user_permissions']