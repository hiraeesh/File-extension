from django.db import models
from django.core.exceptions import ValidationError



class ModelWithFileField3(models.Model):
        fileimg  = models.FileField(upload_to='xyz')