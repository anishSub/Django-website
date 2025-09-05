from django.contrib import admin
from .models import Category
# Register your models here.
class categoryAdmin(admin.ModelAdmin):#Defines a new class called categoryAdmin that inherits from admin.ModelAdmin, which is Django’s base class for customizing the admin interface for a model.
  prepopulated_fields={'slug':('category_name',)}#This line tells Django to automatically populate the slug field in the admin form based on the category_name field. The prepopulated_fields dictionary maps the target field (slug) to the source field(s) (category_name).
  list_display = ('category_name','slug')#Specifies that the admin list view for Category should display two columns: category_name and slug.
  
admin.site.register(Category, categoryAdmin)#Makes the Category model manageable in the admin panel (e.g., at /admin/yourapp/category/) with the prepopulated_fields and list_display configurations.



#* Origin: prepopulated_fields is a specific attribute provided by Django’s admin.ModelAdmin class.  you can name arbitrarily; it has a predefined meaning in the Django admin system.
# What it does: This attribute is used to automatically populate one field (the key) with values derived from another field (the value) when you create or edit an object in the admin interface. In your case, it populates the slug field based on category_name.