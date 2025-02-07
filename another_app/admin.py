from django.contrib import admin
from .models import SomeModel

@admin.register(SomeModel)
class SomeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
