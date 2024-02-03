from django.shortcuts import render
from .models import Mice
from django.contrib.auth.forms import UserCreationForm

def index(request):
    devices = Mice.objects.all()
    return render(request, 'products/index.html', {'devices': devices})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'products/index.html', {'form': form})