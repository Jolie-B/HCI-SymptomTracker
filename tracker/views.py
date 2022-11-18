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

    #mockup just a day in the future, spesifics will be chosen later
    #basically choosen that today is the last day of december
    today = datetime.date(2022, 12, 31)
    context_dict['date'] = today

    dayDataToday,_ = Day.objects.get_or_create(date=today)

    context_dict['todayData'] = dayDataToday
  
    form = DayForm(request.POST, instance=dayDataToday)
    context_dict['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            dayDataToday = form.save(commit=False)
            dayDataToday.save()
            return render(request, 'index.html', context_dict)
        else:
            print(form.errors)
    return render(request, 'index.html', context_dict)



def callendar(request):
    return HttpResponse("Hello, world. You're at the tracker callendar.")


def stats(request):
    return HttpResponse("Hello, world. You're at the tracker stats.")


def date(request, date_slug):

    context_dict = {}

    #mockup just a day in the future, spesifics will be chosen later
    #basically choosen that today is the last day of december
    today, _ = Day.objects.get_or_create(daySlug = date_slug)
    context_dict['date'] = date_slug

    context_dict['todayData'] = today
  
    form = DayForm(request.POST, instance=today)
    context_dict['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            today = form.save(commit=False)
            today.save()
            return redirect(reverse('tool:day', args=[date_slug]))
        else:
            print(form.errors)
    return redirect(reverse('tool:day', args=[date_slug]))

