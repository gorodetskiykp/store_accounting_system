from django.contrib import admin
from .models import Products, Naklads, PriceLists, Customers, Addresses, Volumes, Zakaz


class ProductsAdmin (admin.ModelAdmin) :
	list_display = ('product_name','volume')
	list_display_links = ('product_name',)
	search_fields = ('product_name',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Naklads)
admin.site.register(PriceLists)
admin.site.register(Customers)
admin.site.register(Addresses)
admin.site.register(Zakaz)
admin.site.register(Volumes)