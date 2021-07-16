from django.contrib import admin

from roughwork.models import Workshop


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = 'name', 'host', 'topic', 'complete',
