from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Manager for the  user profiles

    Args:
        BaseUserManager (_type_): _description_

    Returns:
        _type_: _description_
    """

    def create_user(self,email,name,password=None):
        """Create new user profile

        Args:
            email (_type_): _description_
            name (_type_): _description_
            password (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if not email:
            raise ValueError('User need to have a Email')
        email =self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password):
        user = self.create_user(email, name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):

    email= models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''  full name  of user'''
        return self.name
    def get_short_name(self):
        ''' short name of the user'''
        return self.name

    def __str__(self):
        return self.email


class ProfileJournalItem(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title