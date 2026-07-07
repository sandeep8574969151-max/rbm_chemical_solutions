from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    
    def __str__(self):
        return self.title
    
class GeneralProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title 
    
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    features = models.TextField(blank=True, null=True)
    applications = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gallery Image {self.id}"
    
    
class ClientSlider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name        