from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here.


class Entry(models.Model):
    prompt = models.TextField(default="trey")
    body = RichTextField(blank=True, null=True)
    
    @property
    def entry_id(self):
        return self.id
     



 



# print(Entry.__dict__)