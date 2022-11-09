from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_all, name='posts'),
    path('catalog/', views.Catalog, name='catalog'),
    path('about/', views.About, name='about'),
    path('car/<int:item>', views.Car, name='car'),
]