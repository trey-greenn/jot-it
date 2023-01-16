from django import forms 
from .models import Prompt

class EditPrompt(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ('prompt')

        widgets = {
            'prompt' : forms.Textarea(attrs={'class': 'form-control'})
        }


