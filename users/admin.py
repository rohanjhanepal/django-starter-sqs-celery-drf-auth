from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from .models import (
                     User ,
                    )
admin.site.site_header = "LabelApp"
admin.site.site_title = "LabelApp Admin Portal"
admin.site.index_title = "Welcome to LabelApp Portal"


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 
                    'last_name', 'is_staff','is_superuser',
                    'is_active',
                    'last_login','user_date_joined','registration_method',
                    )



admin.site.register(User,CustomUserAdmin) #, UserAdmin)
