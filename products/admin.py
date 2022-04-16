from django.contrib import admin

from products.models import (Products,SubCategory,Category)

# Register your models here.

admin.site.register(Products)
admin.site.register(SubCategory)
admin.site.register(Category)
