from django.http import HttpResponse
from myapp.models import Product
from myapp.models import Manufactory
from django.shortcuts import render


def home(request):
    Data = {'Products': Product.objects.all(),
            'Manufactorys': Manufactory.objects.all()}
    return render(request, 'pages/listsp.html', Data)
