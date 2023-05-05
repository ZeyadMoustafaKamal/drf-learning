from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=70)
    content = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2,default=9.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

