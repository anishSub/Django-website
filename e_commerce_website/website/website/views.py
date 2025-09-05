from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product



def home(request):
  products = Product.objects.all().filter(is_available=True) #this is for quering database and explanation is below 
  
  context = {
    'products': products,
  }
  return render(request,'home.html',context)

#Product – This refers to your model (likely defined in models.py), which maps to a database table (e.g., product).

# .objects – This is the model manager that lets you perform queries on the database.

# .all() – This fetches all rows (records) from the Product table.

# .filter(is_available=True) – This filters the records where the is_available field is set to True.

# ✅ So yes:
# That line is querying the database for all Product objects where is_available=True — and storing the result in the products variable.