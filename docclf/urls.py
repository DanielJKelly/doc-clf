from django.urls import path

from . import views 

urlpatterns = [
  path('', views.index, name='index'),
  path('upload', views.upload_file, name='upload_file'),
  path('results/<str:batch_name>', views.results, name='results'),
  path('results/document/<int:doc_id>', views.document, name='document')
]