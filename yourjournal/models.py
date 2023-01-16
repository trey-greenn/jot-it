from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here.


class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    prompt = models.TextField(default="trey")
    body = RichTextField(blank=True, null=True)
    
     



 



# print(Entry.__dict__)