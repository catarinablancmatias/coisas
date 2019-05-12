from django.contrib import admin
from .models import Profile

#Para o administrador poder gerir na área administrativa os perfis dos utilizadores

admin.site.register(Profile)
