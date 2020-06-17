from django.urls import path
from . import views

# Create your views here

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),


]



