from django.db import models
from store.models import Product, Variation
# Create your models here.
#This is for the cart and cart added models  After making this models we have to register it to admin.py

class Cart(models.Model):
  cart_id = models.CharField(max_length=250, blank=False, null=False)
  date_added = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.cart_id
  
  
class CartItem(models.Model):
  product= models.ForeignKey(Product, on_delete=models.CASCADE)#this product is form store.models A
  variations= models.ManyToManyField(Variation,blank=True)#it is from the carts/views 
  cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  is_active = models.BooleanField(default=True)
  
  def sub_total(self):
    return self.product.price * self.quantity
  
  def __unicode__(self):
    return self.product
  