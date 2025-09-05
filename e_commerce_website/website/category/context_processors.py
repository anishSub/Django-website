# Context processors are Python functions that Django calls to inject additional data into the context of every template rendering, unless explicitly excluded. They run automatically for all render() calls, adding variables to the template context.
# Purpose: They provide a way to make global data (e.g., user info, site settings, or custom variables) available across all templates without manually passing it in every view.

# Example in Your Project
# Current Setup: In your store/views.py, you manually pass context = {'products': products, 'product_count': product_count} to store.html. This works for that view but isn’t global.
# With Context Processors: If you added a custom context processor to include product_count or a category list globally, it would be available in every template (e.g., base.html, store.html) without changing each view.

#* this is for displaying all the categores in the side menu 
from category.models import Category

def menu_links(request):
  #fetch all the categories from databasex #And you alos have to add this into settings. Templates and after adding this meny_links it can be used in any templated ( 'Category.context_processors.menu_links',)
  links = Category.objects.all()
  return dict(links=links)