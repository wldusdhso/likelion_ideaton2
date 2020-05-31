from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=10, default="")
    content = models.TextField() 
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

class Answer(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.CharField(max_length=10, default="")
    question_id = models.IntegerField(default=0)
