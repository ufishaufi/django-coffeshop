from django.contrib import admin

# Register your models here.
from pos.models import Menu, Order, Item

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Item)



