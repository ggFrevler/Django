from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import models


# Carousel
def Carousel(request):
    index = models.Carousel.objects.all()
    return render(request, 'index.html', {'index': index})


# Catalog
def Catalog(request):
    catalog = models.Catalog.objects.all()
    return render(request, 'catalog.html', {'catalog': catalog})


# Car
def Car(request, item):
    car = models.Catalog.objects.get(id=item)

    if request.method == "POST":
        text = request.POST.get("comment_text")
        current_user = request.user
        models.CommentCar.objects.create(username=current_user, comment=car, text=text)

    carType = models.Catalog.CarType.choices[car.carType][1]
    comments = models.CommentCar.objects.filter(comment=car.id)
    return render(request, 'car.html', {'car': car, 'carType': carType, 'comments': comments})


# Search system
def Search(request):
    query = request.GET.get("query")
    catalog = models.Catalog.objects.filter(name__contains=query)
    if (catalog.count() > 0):
        return render(request, 'search.html', {'catalog': catalog})
    else:
        return render(request, 'search_not_found.html')


# About
def About(request):
    return render(request, 'about.html')


# Registration
class Registration(CreateView):
    form_class = UserCreationForm
    success_url = '/users/'
    template_name = 'register.html'

    def get_success_url(self):
        return "/"


# Login
class NewLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return "/"
