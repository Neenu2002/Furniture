from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="Category",null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)

class ProductDB(models.Model):
    Product_Category=models.CharField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)
    Country_of_origin=models.CharField(max_length=100,null=True,blank=True)
    Manufactured_by=models.CharField(max_length=100,null=True,blank=True)
    Image1=models.ImageField(upload_to="Products",null=True,blank=True)
    Image2 = models.ImageField(upload_to="Products", null=True, blank=True)
    Image3 = models.ImageField(upload_to="Products", null=True, blank=True)