from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.Carousel, name='posts'),
    path('catalog/', views.Catalog, name='catalog'),
    path('about/', views.About, name='about'),
    path('car/<int:item>', views.Car, name='car'),
    path('search/', views.Search, name='search'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.NewLoginForm.as_view(), name='login'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
]
