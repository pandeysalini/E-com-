from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
  name=models.CharField(max_length=30)
  description=models.TextField(max_length=300)
  
  class Meta:
    db_table='category'
    
  def __str__(self):
    return self.name
    

class Product(models.Model):
  p_name=models.CharField(max_length=300)
  p_price=models.IntegerField()
  p_description=models.TextField(max_length=300)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  
  class Meta:
    db_table='product'
    
class cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  
  class Meta:
    db_table='cart'
