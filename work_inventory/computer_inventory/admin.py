from django.contrib import admin
from .models import Computer
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ViewAdmin(ImportExportModelAdmin):
    pass

class ComputerAdmin(admin.ModelAdmin):
    search_fields = ['computer_name', 'serial_number', 'user_name', 'person_full_name']
    list_display = ('computer_name', 'serial_number', 'user_name', 'person_full_name')
admin.site.register(Computer, ComputerAdmin)


