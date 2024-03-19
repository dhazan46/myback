from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    img = models.ImageField(null=True,blank=True,default=None)

    def __str__(self):
        return self.name