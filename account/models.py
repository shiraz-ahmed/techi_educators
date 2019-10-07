from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,BaseUserManager
)

class userManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("user must have an email address")
        if not password:
            raise ValueError("user must have a password")
        # if not full_name:
        #     raise ValueError("user must have a name")
        user_obj =self.model(
            email=self.normalize_email(email),
            # full_name = full_name
        )
        user_obj.set_password(password) # same is the way for changing password
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,email,password): # creating the staff member
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
# ,full_name
    def create_superuser(self,email,password): # manually creating the super user
        user = self.create_user(
            email,
            # full_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class user(AbstractBaseUser):
    email = models.EmailField(unique=True,max_length=255)
    name= models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    # active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD= 'email'  #this mean that the authentication will take place through email
    # REQUIRED_FIELDS=[] #email and password are required by default
    objects = userManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True # this is for the permission and if not then this will result into an error

    def has_module_perms(self,app_label):
        return True

    def get_short_name(self):
        return self.email
    def get_full_name(self):
        return self.full_name

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        # "Is the user a admin member?"
        return self.admin

    # @property
    # def is_active(self):
    #     # "Is the user active?"
    #     return self.active
