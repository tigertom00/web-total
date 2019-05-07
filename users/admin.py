from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username',
                    'first_name',
                    'last_name',
                    'email',
                    'city',
                    'country',
                    'phone',
                    'website',
                    'profile_picture'
                    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'city',
            'country',
            'phone',
            'website',
            'profile_picture'
        )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
