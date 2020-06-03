from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings

# Create your models here.
class Question(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vquestion")
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    status = models.CharField(max_length=1, default='S') #투표전(S) 투표중(R) 투표마감(F)
    total_votes = models.IntegerField(default=0)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

