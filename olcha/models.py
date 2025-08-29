from django.db import models
from decimal import Decimal

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/images/')
    slug = models.SlugField(unique=True,null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True
    )

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} => {self.parent.title}"
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=14,decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='products',null=True,blank=True)

    @property
    def discounted_price(self):
        if self.discount:
            return self.price * Decimal( 1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to= 'products/images/')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='images')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.image.url}"