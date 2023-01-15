from django.urls import path, include
from . import views
# int:pk == integer primary key, which is what every blog post get in the database
# from .views import AIPromptView
urlpatterns = [
    # path("", views.home, name="home")
    path("", views.index, name="home")

]