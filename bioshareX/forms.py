from django import forms
from bioshareX.models import Share, SSHKey

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('name', 'notes')
        
class SSHKeyForm(forms.ModelForm):
    class Meta:
        model = SSHKey
        fields = ('name', 'key')
        
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file  = forms.FileField()
    
class FolderForm(forms.Form):
    name = forms.CharField(max_length=100)


