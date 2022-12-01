from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_all, name='posts'),
    path('catalog/', views.Catalog, name='catalog'),
    path('about/', views.About, name='about'),
    path('car/<int:item>', views.Car, name='car'),
    path('search/', views.Search, name='search'),
    path('registration/', views.Register, name='registration'),
    path('login/', views.Login, name='login'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.NewLoginForm.as_view(), name='login'),
]