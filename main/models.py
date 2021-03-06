from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Comp(models.Model):
    name = models.CharField( max_length=50 )
    cpu = models.CharField( max_length = 30 )
    rate = models.IntegerField( )
    price = models.IntegerField()
    desc = models.CharField( max_length=2000, null=True  )
    imageUrl = models.CharField( max_length=100, null=True )
    betUsers = models.ManyToManyField( User )
    
    def __str__(self):
        return "Name = %s, Country = %s, rate = %s" % (self.name, self.cpu, self.rate)


