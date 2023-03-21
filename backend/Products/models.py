from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    price = models.FloatField( )


    @property
    def get_discount(self):
        return self.price*0.5
    
    def sales_price(self):
        return 100

    def __str__(self) -> str:
        return self.title