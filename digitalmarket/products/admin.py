from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "sale_price"]
    search_fields = ["description", "title"]
    list_filter = ["price"]
    list_editable = ["sale_price"]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
