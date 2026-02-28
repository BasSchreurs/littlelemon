from django.contrib import admin
from .models import Menu, MenuItem, Booking

# Inline MenuItems inside Menu
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1  # shows one empty row by default
    fields = ('title', 'price')  # only show these fields

# Menu admin with inline MenuItems
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

# Register Menu with inline MenuItems
admin.site.register(Menu, MenuAdmin)

# Register Booking separately
admin.site.register(Booking)
