from django.db import models

# Create your models here.



class Prompt(models.Model):
    prompt = models.TextField(default="trey")
 
    def __str__(self):
        return self.prompt
