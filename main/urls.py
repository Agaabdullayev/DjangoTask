from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('category', views.category, name='category'),
    path('editProducts/<int:id>', views.editProducts, name='editProducts'),
    path('updatePrices/<int:id>', views.updatePrices, name='updatePrices'),
]