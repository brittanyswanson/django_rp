from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Character(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    species = models.CharField(max_length=200,default="human",null=True)
    bio_text = models.TextField(null=True)

    def __str__(self):
        return self.first_name