from django.shortcuts import render
from django.contrib import messages
from django.core.cache import cache

# Create your views here.

from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from . import util

def index(request):
    return render(request, 'landing.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            util.handle_uploaded_file(request.FILES['file'], request.POST['batch_name'])
            return HttpResponseRedirect('results/%s' % request.POST['batch_name'])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def results(request, batch_name):
    batch_docs = util.get_docs_by_batch(batch_name)
    return render(request, 'results.html', {'batch_docs': batch_docs, 'batch_name': batch_name})