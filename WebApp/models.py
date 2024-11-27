from django.db import models

# Create your models here.
class ContactDB(models.Model):
    First_Name=models.CharField(max_length=100,null=True,blank=True)
    Last_Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Message=models.TextField(max_length=200,null=True,blank=True)

class SignupDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Mail=models.EmailField(max_length=100,null=True,blank=True)
    Mobile=models.TextField(max_length=20,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm=models.CharField(max_length=100,null=True,blank=True)

class CartDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(max_length=100,null=True,blank=True)
    Total_Price=models.IntegerField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)

class orderDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
    Total_price=models.IntegerField(null=True,blank=True)