from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import models
# Create your views here.



def blog_all(request):
    index = models.Karysel.objects.all()
    return render(request, 'index.html', {'index': index})


def Catalog(request):
    catalog = models.Catal.objects.all()
    return render(request, 'catalog.html', {'catalog': catalog})


def Car(request, item):
    car = models.Catal.objects.get(id=item)
    carType = models.Catal.CarType.choices[car.carType][1]
    return render(request, 'car.html', {'car': car, 'carType': carType})

def Search(request):
    query = request.GET.get("query")
    catalog = models.Catal.objects.filter(name__contains=query)
    if (catalog.count() > 0):
        return render(request, 'search.html', {'catalog': catalog})
    else:
        return render(request, 'search_not_found.html')


def About(request):
     return render(request, 'about.html')

class Registration(CreateView):
    form_class = UserCreationForm
    success_url = '/users/'
    template_name = 'register.html'


class NewLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return "/"



