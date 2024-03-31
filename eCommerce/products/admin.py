from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import Category, Product, Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at',
                    'child_category_count',
                    'subcategory_list')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def child_category_count(self, obj):
        return obj.children.count()

    child_category_count.short_description = 'No. of Child Categories'

    def subcategory_list(self, obj):
        children = obj.children.all()
        if children:
            subcategory_links = [
                format_html('<a href="{}">{}</a>', reverse('admin:products_category_change', args=[child.id]), child.name)
                for child in children
            ]
            return mark_safe(', '.join(subcategory_links))
        return '-'

    subcategory_list.short_description = 'Subcategories'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at',
                    'brand', 'stock_quantity')
    list_filter = ('brand', 'stock_quantity', 'price',
                   'available')
    search_fields = ('name', 'brand')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
