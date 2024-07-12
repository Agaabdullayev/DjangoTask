from django.shortcuts import render, redirect, HttpResponse
from . models import Category, Products, Images, Prices
from django.db.models import Count
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

import json
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import os

from django.contrib.auth.models import User, auth

# from django.core.cache import cache
from django.shortcuts import render
from django.db.models import F
from django.utils import timezone

from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'index.html')

def products(request):
    if request.method == 'POST':
        upload = request.FILES['productsImage']
        fs = FileSystemStorage()
        file = fs.save(upload.name, upload)
        file_url = fs.url(file)

        productsName = request.POST['productsName']
        productsPrice = request.POST['productsPrice']
        productsCategory_id = request.POST['productsCategory']
        productsDescription = request.POST['productsDescription']

        category = Category.objects.get(id=productsCategory_id)

        createdProducts = Products.objects.create(
            productsName=productsName,
            productsCategory=category,
            productsDescription=productsDescription
        )

        createdImages = Images.objects.create(
            products=createdProducts,
            productsImage=file_url
        )

        createdPrices = Prices.objects.create(
            products=createdProducts,
            productsPrice=productsPrice
        )

    dataCategory = Category.objects.order_by('id').all()
    dataProducts = Products.objects.order_by('id').all()
    return render(request, 'products.html', {'dataCategory': dataCategory, 'dataProducts': dataProducts})

def editProducts(request, id):
    dataPrices = Prices.objects.order_by('-id').filter(products_id=id)
    
    return render(request, 'editProducts.html', {'dataPrices':dataPrices})

def updatePrices(request, id):
    updatePrice = request.POST['updatePrice']
    
    update = Prices(products_id=id, productsPrice=updatePrice)
    update.save()
    
    return redirect('editProducts', id=id)

def category(request):
    if request.POST:
        category = request.POST['categoryName']
        
        created = Category(categoryName=category)
        created.save()
    
    data = Category.objects.order_by('id').all()
    return render(request, 'category.html', {'data':data})