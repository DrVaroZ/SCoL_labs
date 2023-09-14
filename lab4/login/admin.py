from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()
admin.site.register(User)

list_display = ['first_name', 'last_name', 'date_of_birth',
                'email', 'phone_number', 'id']
