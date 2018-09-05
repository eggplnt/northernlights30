from django.db import models

class Shohin(models.Model):
    hinmoku = models.CharField(max_length=20)
    hinmei  = models.CharField(max_length=100)
    zaiko  = models.IntegerField(default=0)
