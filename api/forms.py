
from django import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

VALID_IMAGE_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png",
    "gif",
]




class UploadFileForm3(forms.Form):
     fileimg = forms.FileField(
           validators=[FileExtensionValidator(VALID_IMAGE_EXTENSIONS)]
                      
        )


