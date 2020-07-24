from django.contrib import admin
from . import models

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    list_per_page = 25
admin.site.register(models.Contact, ContactAdmin)