# ###
# Admin Class for FavouriteBooks model
# ###

from django.contrib import admin
from ecom.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    fieldsets = []
    search_fields = ['id']
