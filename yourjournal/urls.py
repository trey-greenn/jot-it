from django.urls import path, include
from . import views

# from .views import EditEntryView
urlpatterns = [
    # path("", indexx)
    path("", views.indx, name="prompt")
]