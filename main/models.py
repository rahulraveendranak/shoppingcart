from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self): 
        return self.title 


class Product(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField() 

    def __str__(self): 
        return self.title 

class superadmin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self): 
        return self.username 

