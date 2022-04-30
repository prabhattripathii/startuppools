from django.db import models
from django.utils.timezone import now, localtime

# Create your models here.

class ModelForMessages(models.Model):
    Sendername = models.CharField(max_length=50)
    Sendermail = models.CharField(max_length=50)
    Sendersub = models.CharField(max_length=50)
    Sendermess = models.CharField(max_length=50)
    SendingTime = models.DateTimeField(default=now, blank= True)