
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #admin urls
    path('admin/', views.home, name='home'),
    path('admin/list/', views.list, name='list'),
    path('update/<int:product_id>/', views.update, name='update'),
    path('delete/<int:product_id>/', views.delete, name='delete'),  

    path('category/', views.category, name='category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('update_category/<int:category_id>/', views.update_category, name='update_category'), 

    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),



    #user urls
    
    

    #landing url
    path('', views.index, name='index'),
]
