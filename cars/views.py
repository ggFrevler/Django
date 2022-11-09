from django.shortcuts import render

from . import models
# Create your views here.



def blog_all(request):
    index = models.Karysel.objects.all()
    #return "HELLO"
    return render(request, 'index.html', {'index': index})


def Catalog(request):
    catalog = models.Catal.objects.all()
    return render(request, 'catalog.html', {'catalog': catalog})


def About(request):
     about = models.Catal.objects.all()
     return render(request, 'about.html', {'about': about})
