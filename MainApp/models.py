from django.db import models

# Create your models here.


class File(models.Model):
    file = models.FileField(upload_to = "files")
    

class Time_interval(models.Model):
    time_interval = models.CharField(max_length =100)


class Candle(models.Model):
    Index_name = models.CharField(max_length =100)
    # date = models.DateField()
    date = models.CharField(max_length =100)
    time = models.CharField(max_length =100)
    open = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    volume = models.IntegerField(default=0)