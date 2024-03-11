from django.contrib import admin
from goobusinessesapp.models import AllServices
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class AllServicesV(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('name','slID','selectImage','homepagecatagori','date')
admin.site.register(AllServices,AllServicesV)
