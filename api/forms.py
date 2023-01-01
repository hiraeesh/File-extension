
from django import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

VALID_IMAGE_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png",
    "gif",
]


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 1024:
        raise ValidationError("You cannot upload file more than Mb")
    else:
        return value



class UploadFileForm3(forms.Form):
     fileimg = forms.FileField(
           validators=[FileExtensionValidator(VALID_IMAGE_EXTENSIONS),validate_file_size],
                      
        )


