from hashlib import new
import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from tracker.models import *
from django.db.models import Sum, F

import datetime

from tracker.forms import *


def index(request):
    context_dict = {}
    context_dict['data'] = Day.objects.all()



    return render(request, 'index.html', context_dict)


def stats(request):
    return HttpResponse("Hello, world. You're at the tracker stats.")


def date(request, day_slug):
    context_dict = {}

    day = day_slug[0:2]
    month = day_slug[2:4]
    year = "20" + day_slug[4:6]
    context_dict['date'] = day + "/" + month + "/" + year; 

    if Day.objects.filter(date = day_slug).exists():
        context_dict['existing_data'] = Day.objects.filter(date = day_slug)
        print("exists", context_dict['existing_data'])

    return render(request, 'day.html', context=context_dict)



def save_data(request):
    if request.method == 'POST':
        request.POST._mutable = True

        p = request.POST['date']
        print(p)
        dd = p[0:2]
        mm = p[3:5]
        yy = p[8:10]
        request.POST['date'] = dd+mm+yy
    
        form = DayForm(request.POST)
        if form.is_valid():
            data = form.save(commit=True)
        else:
            cleaned = form.cleaned_data
            if Day.objects.filter(date = request.POST['date']).exists():
                # already exists, so update existing values
                obj = Day.objects.filter(date = request.POST['date']);
                obj.update(
                    dairy = cleaned['dairy'],
                    gluten = cleaned['gluten'],
                    sugar = cleaned['sugar'],  
                    fatigue = cleaned['fatigue'],
                    nausea = cleaned['nausea'],
                    bloated = cleaned['bloated'],  
                )
    
    return redirect(reverse('index'))