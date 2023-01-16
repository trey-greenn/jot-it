from django.shortcuts import render, redirect
from .models import Entry
from .forms import PostEntry
from django.views.generic import ListView
from aiprompt.models import Prompt
# Create your views here.



# text box
# ListView
# class EditEntryView(ListView):
#     model = Entry
#     # form_class =  PostEntry
#     fields = ["body" ]


def indx(request):
    script = Entry.objects.all()
    form = PostEntry()
    return render(request, "entries/entries.html", {"script" : script, "form": form})


# def PromptList(request):

#     if request.method == "GET":
#         prompt = Entry.objects.all()
#         context = {'prompt':prompt}
#         return render(request, 'entries/entries.html', context)
    
#     if request.method == "POST":
#         entry = Entry.objects.create(
#             body=request.POST.get('body')
#         )
#         entry.save()
#         return redirect('prompt')

        


