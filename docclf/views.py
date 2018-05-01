from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .util import handle_uploaded_file

def index(request):
    return HttpResponse('Hello, welcome home')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print('request: ', request.FILES)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print('in form is valid block')
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html' )