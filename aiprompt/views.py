from django.shortcuts import render
from .models import Prompt

# Create your views here.

# class AIPromptView(ListView):
#     model = Prompt
#     template_name = "aiprompt.html"
#     # paginate_by = 1
#     # ordering = ['post_date']
#     # ordering = ['-id']

def index(request):
    prompt = Prompt.objects.all()
    return render(request, "prompts/aiprompt.html", {"prompt" : prompt})





