from importlib.metadata import files

from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    estates = Estate.objects.filter(sold=False, area__gte=100).all()
    return render(request, 'index.html', context={'estates': estates})

def edit(request, eid):
    estate = Estate.objects.filter(pk=eid).first()
    if request.method == 'POST':
        form = EstateForm(request.POST, files=request.FILES, instance=estate)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = EstateForm(instance=estate)
    return render(request, 'edit.html', context={'estate': estate, 'form': form})