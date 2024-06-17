from django.db import models
from django.shortcuts import reverse

# this model make category for products
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

# this model make vendor for products
class Vendor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    # this is size of product for user choice
    PRODUCT_SIZE = [
        ('1', 'XS'),
        ('2', 'S'),
        ('3', 'M'),
        ('4', 'L'),
        ('5', 'XL'),
        ('6', 'XXL'),
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    size = models.CharField(max_length=10, choices=PRODUCT_SIZE, blank=True)

    quantity = models.IntegerField(default=0)
    last_updated = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])
        

class Images (models.Model):
    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
