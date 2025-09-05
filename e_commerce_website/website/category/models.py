from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)
  slug=models.SlugField(max_length=100, unique=True)
  description=models.TextField(max_length=255, blank=True)#Textfield allows larger text than charfield
  cat_image=models.ImageField(upload_to='photos/categories', blank=True)
  
# class Category(models.Model):
# What it does: This line defines a new class called Category that inherits from models.Model. In Django, models.Model is the base class for all models, providing functionality to interact with the database (e.g., creating tables, saving data).
  class Meta:
    verbose_name='category'
    verbose_name_plural='categories'
    # By default, Django applies a pluralization rule to the model name. So, Category becomes Categories in the admin interface (e.g., under the "Categorys" which is mistake so we can make it correct my writing this line of code  section where you can add or edit categories).
    
    #this id for displaying categories 
  def get_url(self):
      return reverse('products_by_category', args = [self.slug])
      
      
#Return Statement: return reverse('products_by_category', args=[self.slug])
# What it does: The reverse function is a Django utility that resolves a URL pattern name into an actual URL path. Here, it:
# Takes the name of a URL pattern ('products_by_category').
# Uses args=[self.slug] to provide the slug (e.g., "shirts") as an argument to the URL pattern.
# Returns the resulting URL (e.g., /store/shirts/).
#products_by_category is in urls.py of store 

#*Overall Purpose
# What it does: The get_url method generates a URL for the category page based on the instance’s slug. This URL can be used to link to the category’s product list (e.g., in a template or view).
# Example Usage:
# In a template: {{ category.get_url }} would output /store/shirts/ for a Category named "Shirts".
# In a view: You could call category.get_url() to redirect or link to that page.
# Benefit: It abstracts the URL generation, making it reusable and decoupled from hardcoding URLs.
    
  def __str__(self):
    return self.category_name
  
#* When you define a method inside a class (like __str__), Python needs to know which object’s data to work with. Since multiple categories can exist (e.g., "Books," "Clothing"), self helps the method know which category’s data to access.It’s like saying, "Use the data from the category I’m dealing with right now.

