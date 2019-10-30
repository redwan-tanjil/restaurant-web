from django.db import models


# Create your models here.
#model for subscriber
class Subscriber(models.Model):
    email = models.CharField(max_length=255)


#model for email
class Massage(models.Model):
    text = models.CharField(max_length=5555)
    sub = models.CharField(max_length=255)
    num = models.IntegerField(default=1)

