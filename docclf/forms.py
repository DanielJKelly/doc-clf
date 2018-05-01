from django import forms 

class UploadFileForm(forms.Form):
    file = forms.FileField
    batch_name = forms.CharField(label='Batch Name', max_length=50)