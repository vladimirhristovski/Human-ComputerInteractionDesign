from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    estates = Estate.objects.filter(sold=False, area__gte=100)
    context = []
    for estate in estates:
        price = 0
        estates_characteristics = EstatesCharacteristics.objects.filter(estate=estate)
        for estate_characteristic in estates_characteristics:
            price += estate_characteristic.characteristic.price
        context.append({'estate': estate, 'price': price})

    return render(request, 'index.html', context={'context': context})


def edit(request, estate_id):
    estate = Estate.objects.filter(id=estate_id).first()
    if request.method == 'POST':
        form = EstateForm(request.POST, files=request.FILES, instance=estate)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = EstateForm(instance=estate)
    return render(request, 'edit.html', {'form': form, 'estate': estate})
