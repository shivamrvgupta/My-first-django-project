from django.contrib import admin
from . import models

# Register your models here.

class RelatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('email',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(models.Relator, RelatorAdmin)