from django.contrib import admin
from inventario.models import Product, Category

admin.site.register(Category)
admin.site.register(Product)