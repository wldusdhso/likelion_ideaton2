from django.db import models
from django.conf import settings
# Create your models here.

class Decision(models.Model):
    choice_content = models.CharField(max_length=200)
    maker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    result = models.BooleanField(default=True)

    def __str__(self):
        return self.choice_content 

