from django import forms 
from .models import Prompt

class EditPrompt(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ('title', 'prompt')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type here'}),
            # 'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'author' : forms.Select(attrs={'class': 'form-control'}),
            'prompt' : forms.Textarea(attrs={'class': 'form-control'})

        }
