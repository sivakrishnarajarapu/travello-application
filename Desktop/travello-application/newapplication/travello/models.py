from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=10)
    desc = models.TextField()
    img = models.ImageField(upload_to='imgs')
    price = models.IntegerField()
    offer = models.BooleanField()