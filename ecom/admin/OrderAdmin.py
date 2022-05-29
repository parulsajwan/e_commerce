# ###
# Admin Class for LikedBook model
# ###

from django.contrib import admin
from ecom.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    model = Order
    fieldsets = []
    search_fields = ['id']
