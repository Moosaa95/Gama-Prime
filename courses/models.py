from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Programming(models.Model):
    ''' 
        databse programming courses 
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    # image = CloudinaryField('image')
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_enroll = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"{self.slug}"


class Business(models.Model):
    ''' 
        databse business courses 
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_enroll = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)



    def __str__(self):
        return self.name
    


class Design(models.Model):
    ''' 
        databse design courses 
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_enroll = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"{self.slug}"

class Management(models.Model):
    ''' 
        databse management courses 
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_enroll = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)



    def __str__(self):
        return self.name