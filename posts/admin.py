# 2:
from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'published']


'''
. Estando en el paso 2, hacer estos dos comandos:
1. python manage.py makemigrations
2. python manage.py migrate
'''