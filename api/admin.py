from django.contrib import admin
from api.models import ModelWithFileField3
# Register your models here.

@admin.register(ModelWithFileField3)

class Uploaddata(admin.ModelAdmin):
    list_display=['fileimg']
