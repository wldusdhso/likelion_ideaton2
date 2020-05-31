from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=20)
    #writer = models.ForeignKey(to,on_delete)
    content = models.TextField() 
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    # def summary(self):
    #     return self.content[:100]

# class Ansewer(models.Model):
#     content = models.TextField()
#     pub_date = models.DateTimeField()
    # writer = models.ForeignKey()

# writer는 어떻게 작성해야하는강?