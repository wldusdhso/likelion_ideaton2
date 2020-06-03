from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=20)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField() 
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

class Answer(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question_id = models.IntegerField(default=0)
