from django.db import models
from datetime import datetime

# Create your models here
class Post(models.Model):
    Headline = models.CharField(max_length=255)
    Description = models.CharField(max_length=1000000000)
    Date_Posted = models.DateTimeField(default = datetime.now(), blank= True)



