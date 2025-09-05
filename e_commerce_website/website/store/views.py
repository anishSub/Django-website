from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from carts.views import _cart_id, CartItem
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.
def store(request,category_slug=None):
  categories =None
  products=None
  
  if category_slug != None:
    categories = get_object_or_404(Category, slug = category_slug)
    products = Product.objects.filter(category=categories, is_available=True)
    paginator = Paginator(products,1)#show 6 products in one page 
    page= request.GET.get('page')
    paged_products = paginator.get_page(page)#those 6 produstc are stored here 
    product_count = products.count()
  else:
    products = Product.objects.all().filter(is_available=True).order_by('id') #this is for quering database explanation is below 
    paginator = Paginator(products,3)#show 6 products in one page 
    page= request.GET.get('page')
    paged_products = paginator.get_page(page)#those 6 produstc are stored here 
    product_count = products.count()
  
  context = {
    'products': paged_products,
    'product_count': product_count
  }
  return render(request,'store/store.html', context)

#Product – This refers to your model (likely defined in models.py), which maps to a database table (e.g., product).

# .objects – This is the model manager that lets you perform queries on the database.

# .all() – This fetches all rows (records) from the Product table.

# .filter(is_available=True) – This filters the records where the is_available field is set to True.

# ✅ So yes:
# That line is querying the database for all Product objects where is_available=True — and storing the result in the products variable.



def product_detail(request, category_slug, product_slug):#The parentheses () after def product_detail contain the list of parameters (or arguments) that the function accepts. These are the inputs the function needs to do its job.
  try:
    single_product = Product.objects.get(category__slug = category_slug,slug= product_slug )#we have to access category and slug of that category.
    in_cart= CartItem.objects.filter(cart__cart_id = _cart_id(request), product=single_product).exists()

  except Exception as e:
    print(f"Error: {e}")
    raise e 
    
  context = {
    'single_product': single_product,
    'in_cart': in_cart,
  }  
  return render(request, 'store/product_detail.html', context)

  
#*What it does: The double underscore (__) in category__slug is used in Django’s ORM to perform a lookup across related models. It allows you to query a field in a related model (e.g., a foreign key or many-to-many relationship) instead of just the current model.
# Explanation for Beginners:
# Imagine you have a Product model that’s linked to a Category model (e.g., a product like "RXEV Blue shirt" belongs to the "Shirts" category).
# The category field in Product is likely a ForeignKey to Category, meaning each product has one category.
# category__slug tells Django, “Look at the category related to this product, and then check its slug field.”
# Purpose: This lets you filter or get objects based on data in a related table without manually joining them.


def search(request):
  if 'keyword' in request.GET:
    keyword=request.GET['keyword']
    if keyword:#if keyword has something
      products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q( product_name__icontains=keyword))#here the Q menas the query set used in DB for or operator 
      product_count = products.count()
  context={
    'products': products,
    'product_count':product_count,
  }
      
  return render(request, 'store/store.html', context)