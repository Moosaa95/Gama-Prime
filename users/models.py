import email
from django.db import models
from PIL import  Image
# extend from BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


# Create your models here.


class UserManger(BaseUserManager):
    """
        create a user with the given email and password

    Args:
        BaseUserManager (type): 
    """    
    def create_user(self, first_name, last_name, email, profile_pic='no-image', password=None, is_admin=False, is_active=True, is_staff=False, is_superuser=False):
        """

            Creates and saves a User with the given details

        Args:
            first_name (CharField): user's first name
            last_name (CharField): user's last name
            email (EmailField): user's email
            profile_pic (ImageField): user's profile picture
            password (CharField): user's password
            is_admin (BooleanField): user's admin status
            is_staff (BooleanField): user's staff status
            is_superuser (BooleanField): user's superuser status
        """     

        # check or validate the email
        if not email:
            raise ValueError('Users must have an email address')

        # check or validate the password
        if not password:
            raise ValueError('Users must have a password')

        # check or validate the first name
        user_obj = self.model(
            first_name=first_name,
            last_name=last_name,
            profile_pic=profile_pic,
            email=self.normalize_email(email), # convert all email to lowercase
        )   
        user_obj.set_password(password) # set and hashes the password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.superuser = is_superuser

        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, first_name, last_name, email,  password=None):
        """
            Creates and saves a staff user with the given details

        Args:
            first_name (CharField): staff's first name
            last_name (CharField): staff's last name
            email (EmailField): staff's email
            password (CharField): staff's password
        """     
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
            is_staff=True,
        )
        return user
    
    def create_superuser(self, first_name, last_name, email,  password=None):
        """
            Creates and saves a superuser with the given details

        Args:
            first_name (CharField): superuser's first name
            last_name (CharField): superuser's last name
            email (EmailField): superuser's email
            password (CharField): superuser's password
        """     
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True,
        )
        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    """
       extends from AbstractBaseUser, PermissionsMixin
         add custom fields
    

    Args:
        AbstractBaseUser (type):  AbstractBaseUser - Django's default user model
        PermissionsMixin (type):  PermissionsMixin - Django's default user model
    """   
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    ) 
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    # email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    profile_pic = models.ImageField(upload_to="images", blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    superuser = models.BooleanField(default=False) # a superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserManger()

    USERNAME_FIELD = 'email' # username
    REQUIRED_FIELDS = ['first_name', 'last_name'] # required fields


    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_active(self):
        return self.active
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)




class Profile(models.Model):
    """
        add custom fields
    """
    GENDER_CHOICES = (
        ('M','Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    education = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    # education_start = models.DateField(blank=True, null=True)
    # education_end = models.DateField(blank=True, null=True)
    year = models.CharField(max_length=50, blank=True)
    # track = models.CharField(max_length=50, blank=True)
    # speciality = models.CharField(max_length=50, blank=True)
    professional_summary = models.TextField(blank=True)
    title = models.CharField(max_length=50, blank=True)



    
    def __str__(self):
        return str(self.user.email)

    
    # overwrite the save method it gets run after our method is saved
    # def save(self, *args, **kwargs):
    #     """
    #         overwrite the save method it gets run after our method is saved
    #     """        
    #     super.save(*args, **kwargs)

    #     img = Image.open(self.image.path) # open the image

    #     if img.height > 300 or img.width > 300: # check if the image is greater than 300x300
    #         output_size = (300, 300) # set the output size
    #         img.thumbnail(output_size) # resize the image
    #         img.save(self.image.path) # save the image
        

