from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account
# Register your models here.

#Since Account is a custom user model, UserAdmin provides a foundation (e.g., password handling, user lists), and AccountAdmin tailors it to your fields (e.g., email, phone_number).
class AccountAdmin(UserAdmin):
  
  list_display = ('email','first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active' )# this is for not  diaplaying password and changing is not possible so you have to reset it  #And Specifies the fields to display as columns in the admin list view for Account objects. It includes email, first_name, last_name, username, last_login, date_joined, and is_active.By not including password in list_display, you can’t see or edit it directly in the list, forcing a reset if needed (e.g., via python manage.py changepassword).
  
  
  # Makes the email, first_name, and last_name fields clickable links in the list view, taking you to the edit page for that user.
  list_display_links = ('email', 'first_name', 'last_name') 
  readonly_fields = ('last_login', 'date_joined')
  ordering = ('-date_joined',)#Orders the list of users by date_joined in descending order (newest first, due to the - prefix).
  
  
  filter_horizontal = ()#Defines a tuple of fields to use a horizontal filter widget (e.g., for many-to-many relationships). Here, it’s empty.
  list_filter = ()#Specifies fields to filter the user list by (e.g., a sidebar filter). Here, it’s empty.
  fieldsets = ()
  
  
admin.site.register(Account, AccountAdmin)#Makes the Account model manageable in the admin panel (e.g., at /admin/) with the settings defined in AccountAdmin.Connects your custom user model to the admin interface. Registers the Account model with the admin site, using the AccountAdmin class for customization.