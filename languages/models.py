from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Language(models.Model):
    Lang_Name = models.CharField(max_length=255)
    Programmer= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Description = models.CharField(max_length=255)
    


    def __str__(self):
        return self.Lang_Name
