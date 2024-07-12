from django.db import models
import time
import datetime as d
from math import ceil

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Products(models.Model):
    productsName = models.CharField(max_length=255)
    productsCategory = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    productsDescription = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Images(models.Model):
    products = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    productsImage = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Prices(models.Model):
    products = models.ForeignKey(Products, related_name='prices', on_delete=models.CASCADE)
    productsPrice = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)