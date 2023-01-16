from django.shortcuts import render
from .models import Prompt
from django.core.paginator import Paginator

# Create your views here.

# class AIPromptView(ListView):
#     model = Prompt
#     template_name = "aiprompt.html"
#     # paginate_by = 1
#     # ordering = ['post_date']
#     # ordering = ['-id']

def index(request):
    prompt = Prompt.objects.all()
    p = Paginator(prompt, 1)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
 
    return render(request, "prompts/aiprompt.html", {"prompt": prompt, "page_obj" : page_obj})





