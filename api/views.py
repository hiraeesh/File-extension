from django.shortcuts import render
from .forms import UploadFileForm3
from .models import ModelWithFileField3
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
def index3(request):
    if request.method == 'POST':
    
      fm = UploadFileForm3(request.POST, request.FILES)

      if fm.is_valid():
        instance = ModelWithFileField3(fileimg=request.FILES['fileimg'])
        instance.save()
        return HttpResponse("File uploaded successfuly")  
    else:
        fm =UploadFileForm3()  
    return render(request,"acb.html",{'fm':fm})     

