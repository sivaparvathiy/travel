from django.db import models

class bookingdata(models.Model):
    name = models.CharField(max_length=100)
    from_to = models.CharField(max_length=100)
    froms = models.CharField(max_length=100)
    date = models.DateTimeField()
    number = models.BigIntegerField()
    sit_nmuber = models.IntegerField()
