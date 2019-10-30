from django.db import models



class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    num = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    guest = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

