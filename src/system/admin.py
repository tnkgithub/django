from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from .models import ImageCsvModel

# Register your models here.
class ImageResource(resources.ModelResource):
    class Meta:
        model = ImageCsvModel
        fields = ('id', 'image_name', 'title')
        import_id_fields = ['id']


class ImageAdmin(ImportExportActionModelAdmin):
    list_display  = (
        'image_name',
        'title'
    )

    resource_class = ImageResource
    formats = [base_formats.CSV]

admin.site.register(ImageCsvModel, ImageAdmin)