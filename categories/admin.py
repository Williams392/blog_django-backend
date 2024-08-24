from django.contrib import admin
from categories.models import Category

# Para q se visualize en el admin:
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']