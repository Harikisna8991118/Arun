from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    _id = models.AutoField(primary_key=True,editable=False)
    name = models.CharField(max_length = 200, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True , default='/place.png')
    price = models.DecimalField(max_digits=7,decimal_places = 2,null=True, blank=True)
    countInStock = models.IntegerField(null = True, blank=True,default=0)
    

    def __str__(self):
        return self.name
        
