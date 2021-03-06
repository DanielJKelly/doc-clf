from django.shortcuts import render
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
    accuracy = util.get_mean_accuracy(batch_docs)
    original_file_name = batch_docs[0].original_file_name
    return render(request, 'results.html', {'batch_docs': batch_docs, 'batch_name': batch_name, 'original_file_name': original_file_name, 'accuracy': accuracy})

def document(request, doc_id): 
    doc = util.get_doc_by_id(doc_id)
    return render(request, 'document.html', {'doc': doc})