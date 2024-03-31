from django.contrib import admin
from .models import Category

class CategoryManagement(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

admin.site.register(Category, CategoryManagement)
