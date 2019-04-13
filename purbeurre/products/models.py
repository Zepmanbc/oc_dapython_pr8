from django.db import models
# from django.contrib.auth.models import User
from purbeurre import settings

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    nutrition_grades = models.CharField(max_length=1)
    fat = models.CharField(max_length=8)
    fat_100g = models.DecimalField(max_digits=3, decimal_places=1)
    saturated_fat = models.CharField(max_length=8)
    saturated_fat_100g = models.DecimalField(max_digits=3, decimal_places=1)
    sugars = models.CharField(max_length=8)
    sugars_100g = models.DecimalField(max_digits=3, decimal_places=1)
    salt = models.CharField(max_length=8)
    salt_100g = models.DecimalField(max_digits=3, decimal_places=1)
    image_url = models.URLField()
    url = models.URLField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name


# class User(models.Model):
#     email = models.EmailField()
#     name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)

#     def __str__(self):
#         return self.email


class Substitute(models.Model):
    product_id = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE)
    substitute_id = models.ForeignKey(
        Product, related_name='substitute', on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('product_id', 'substitute_id', 'user_id'),)
