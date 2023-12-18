from django.shortcuts import render
from .models import Mice

def index(request):
    device = Mice.objects.all()
    return render(request, 'products/index.html', {"device" : device})

