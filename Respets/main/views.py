from django.shortcuts import render
from .models import Animal


def Home(request):
    animal = Animal.objects.all().order_by('animalid')[:10]


    animaldic = {"animal":animal}

    return render (request,'main.html', animaldic)




# Create your views here.
