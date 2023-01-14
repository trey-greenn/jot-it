from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView
from aiprompt.models import Prompt
# Create your views here.



# text box
# ListView
class EditEntryView(ListView):
    model = Entry
    # form_class =  PostEntry
    fields = ["body" ]
    template_name = "entries/entries.html"

# def indexx(request):
#     entry = Entry.objects.all()
#     return render(request, "entries/entries.html", {"ents" : entry})









        


