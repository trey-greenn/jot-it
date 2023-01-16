from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Entry(models.Model):
    write = models.TextField(default="trey")

    
     



 



# print(Entry.__dict__)