from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import urls
from phone_field import PhoneField
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    manager = models.CharField(max_length=128)


class ContactType(models.Model):
    contact_type = models.CharField(max_length=128)

class ContactResult(models.Model):
    contact_result= models.CharField(max_length=128)

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType,on_delete=models.SET_NULL , null=True)
    contact_time = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    result = models.ForeignKey(ContactResult , on_delete= models.SET_NULL,null=True)