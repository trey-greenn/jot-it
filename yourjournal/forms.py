from django import forms 
from .models import Entry

class PostEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ( 'body', 'prompt' ) 

        widgets = {
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'prompt' : forms.Textarea(attrs={'class': 'form-control'})
        }
