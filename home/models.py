from django.db import models


DROP_CHOICE = (
    ("Laptop","Laptop"),
    ("Mouse","Mouse"),
    ("Desktop","Desktop"),
    ("Printer","Printer"),
)

# Create your models here.
class Registration(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(default='')
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname
    

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Entry(models.Model):
    assetname = models.CharField(max_length=50) 
    assetserialNo = models.IntegerField()
    assetmanufacturer = models.CharField(max_length=50)
    date = models.DateField(null=True)
    dropdown = models.CharField(max_length=20, choices = DROP_CHOICE, default= ' ')

    def __str__(self):
        return self.assetname
    
class Restaurant(models.Model):
    Date_of_Purchase = models.DateField(null=True)
    No_of_Dishes = models.IntegerField(blank=True )
    No_of_Spoon = models.IntegerField()
    Water_bottles = models.IntegerField()
    No_of_Fans = models.IntegerField(blank=True) 


    

    