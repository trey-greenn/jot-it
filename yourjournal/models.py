from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Entry(models.Model):
    write = models.TextField(default="trey")
    body = RichTextField(blank=True, null=True)

    
     



 



# print(Entry.__dict__)