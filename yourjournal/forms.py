from django import forms 
from .models import Entry

class PostEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('write',) 

        widgets = {
            'write' : forms.Textarea(attrs={'id': 'common_input_val','class': 'form-control'})
        }
