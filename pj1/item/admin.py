from django.contrib import admin

# Register your models here.

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    list_display_links = ('id',)

admin.site.register(Item, ItemAdmin)
