from django.urls import path, include
# from .views import indexx

from .views import EditEntryView
urlpatterns = [
    # path("", indexx)
    path("", EditEntryView.as_view(), name="entries")
]