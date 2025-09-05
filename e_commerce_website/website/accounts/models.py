from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager): #Defines a new class called MyAccountManager that inherits from BaseUserManager, which is    a                                          base class provided by Django for custom user managers.
  
  #for normal user
  def create_user(self,first_name, last_name, username, email, password=None):#Provides a way to create a new user with the required fields, with password being optional (e.g., for cases where it’s set later).
    if not email:
      
      raise ValueError("user must have email address")
    
    if not username:
      raise ValueError("user must have email username")
    
    
    #Creates a new instance of the Account model using the manager’s model attribute, which refers to the Account class.
    #This is where the user object is initialized with the provided data before saving it to the database.
    #Sets up the user with the fields passed to the method.
    user = self.model(
      email=self.normalize_email(email),#Ensures email consistency (e.g., "USER@EXAMPLE.COM" becomes "user@example.com") to avoid duplicate accounts due to case differences.
      username= username, #Assigns the username parameter to the username field of the user object.
      first_name = first_name,
      last_name = last_name,
    )
    
    user.set_password(password) #Hashes the password and sets it for the user object using Django’s password hashing system.
    user.save(using=self._db)#Saves the user object to the database using the current database connection (self._db).
    return user
  
  
  #for creating super user
  def create_superuser(self, first_name, last_name, email, username, password):
    user=self.create_user(
                          email=self.normalize_email(email),
                          username=username,
                          password=password,
                          first_name=first_name,
                          last_name=last_name,
                          )
    user.is_admin = True #Grants administrative privileges beyond the default admin setup.
    user.is_active = True
    user.is_staff = True
    user.is_superadmin = True
    user.save(using=self._db)



class Account(AbstractBaseUser):# By using class Account(AbstractBaseUser), you’re telling Django that Account will be a custom version of the user model, tailored to your needs (e.g., for your e_commerce_website).
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  username = models.CharField(max_length=50,unique=True)
  email=models.EmailField(max_length=100, unique=True)
  phone_number = models.CharField(max_length=50)
  
  #required
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now_add=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  is_superadmin = models.BooleanField(default=False)
  
#is_admin = models.BooleanField(default=False)
# What it does: This is a boolean field that indicates if the user has administrative privileges (beyond the default admin setup).
# Why default=False?:
# Security: You don’t want every new user to automatically have admin powers. Admin access should be granted manually to trusted users.
# Control: It allows you to decide who gets admin rights, rather than assuming everyone does.
# Logic: Setting it to False by default means new users start with no special admin status unless you explicitly change it.

  USERNAME_FIELD ='email' # 'email': Tells Django to use email as the field for logging in instead of the default username.
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']#Lists fields that must be provided when creating a superuser (e.g., via createsuperuser).
  objects= MyAccountManager()
  
# What Does objects = MyAccountManager() Mean?
# What it Does
# objects is the default manager for a Django model. It’s how you interact with the model’s database objects (e.g., creating, retrieving, or deleting users).
# By setting objects = MyAccountManager(), you replace the default manager (models.Manager) with a custom manager class called MyAccountManager.
# This custom manager defines how users are created (e.g., create_user and create_superuser).
  
  
# A manager in Django is like a "toolset" that handles database operations for a model. The default objects manager lets you do things like Account.objects.all() to get all users.
# A custom manager (like MyAccountManager) lets you add custom logic, such as validating data or setting default values during creation.
  
  

  def __str__(self):
      return self.email
#Overrides the default string representation of an Account object to return the email (e.g., "admin@example.com").
#Makes it easier to identify users in the admin interface or logs by showing their email instead of something like <Account object at 0x...>.
    
  def has_perm(self, perm, obj=None):
    return self.is_admin
# What it does: This method checks if the user has a specific permission (perm) for an object (obj). It returns True if is_admin is True, False otherwise.
# Why: Required by AbstractBaseUser to integrate with Django’s permission system. It simplifies permissions by tying them to the is_admin flag.
# Logic: If a user is an admin, they get all permissions; otherwise, they get none. This is a basic implementation—real apps might check a permission database.
  
  
  def has_module_perms(self, add_label):
    return True
#Checks if the user has permission to access a module (e.g., an app in the admin). It always returns True.
# Why: Another required method for AbstractBaseUser. Returning True means any user with this model can see all modules in the admin, but access to actions (e.g., edit) depends on has_perm.
# Logic: This is a permissive default. In a real app, you might restrict it based on is_staff or other conditions.


