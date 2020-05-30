from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

