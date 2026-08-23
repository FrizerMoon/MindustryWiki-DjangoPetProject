from django.contrib import admin
from .models import ModelInfo

@admin.register(ModelInfo)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description','img']
    prepopulated_fields = {'slug':['name']}
