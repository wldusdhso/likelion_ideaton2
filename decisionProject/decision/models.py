from django.db import models

# Create your models here.

class Decision(models.Model):
    question = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.question 

