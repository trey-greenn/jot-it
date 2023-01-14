from django.shortcuts import render
from django.views.generic import ListView
from .models import Prompt

# Create your views here.

# class AIPromptView(ListView):
#     model = Prompt
#     template_name = "aiprompt.html"
#     # paginate_by = 1
#     # ordering = ['post_date']
#     # ordering = ['-id']

def index(request):
    prompts = Prompt.objects.all()
    # paginate_by = 1, now how can I paginate the pages
    return render(request, "prompts/aiprompt.html", {"prompts" : prompts})


# print(Prompt.objects.all())


