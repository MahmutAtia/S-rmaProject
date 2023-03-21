from Products.models import Product

def run():
    Product.objects.create(title = "toy", content = "heloo",
                          price= 29 )
    Product.objects.create(title = "glass", content = "hali heloo",
                          price= 20 )
    