from django.contrib import admin
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug':('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name', )}
	
	list_display = ['id', 'name', 'price', 'available', 'created', 'updated']
	list_filter = ['price', 'available']
	list_editable = ['price', 'available']