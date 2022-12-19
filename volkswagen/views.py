from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.views import generic
from . import models


# Carousel
def Carousel(request):
    index = models.Carousel.objects.all()
    footer = models.Footer.objects.all()[0]
    return render(request, 'index.html', {'index': index, 'footer': footer})


# Catalog
def Catalog(request):
    catalog = models.Catalog.objects.all()
    footer = models.Footer.objects.all()[0]
    return render(request, 'catalog.html', {'catalog': catalog, 'footer': footer})


# Car
def Car(request, item):
    car = models.Catalog.objects.get(id=item)
    footer = models.Footer.objects.all()[0]


    if request.method == "POST":
        text = request.POST.get("comment_text")
        current_user = request.user
        models.CommentCar.objects.create(username=current_user, comment=car, text=text)


    carType = models.Catalog.CarType.choices[car.carType][1]
    comments = models.CommentCar.objects.filter(comment=car.id)
    return render(request, 'car.html', {'car': car, 'carType': carType, 'comments': comments, 'footer': footer})


# Search system
def Search(request):
    query = request.GET.get("query")
    catalog = models.Catalog.objects.filter(name__contains=query)
    footer = models.Footer.objects.all()[0]

    if (catalog.count() > 0):
        return render(request, 'search.html', {'catalog': catalog, 'footer': footer})
    else:
        return render(request, 'search_not_found.html',{'footer': footer})


# About
def About(request):
    footer = models.Footer.objects.all()[0]
    return render(request, 'about.html', {'footer': footer})


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

