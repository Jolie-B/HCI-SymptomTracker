from hashlib import new
import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from tracker.models import *
from django.db.models import Sum, F
from django.core import serializers
import json

import datetime

from tracker.forms import *


def index(request):
    context_dict = {}
    context_dict['data'] = Day.objects.all()



    return render(request, 'index.html', context_dict)


def stats(request):
    context_dict = {}
    context_dict['display'] = "none"

    return render(request, 'stats.html', context_dict)


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



def statsload(request):
    date_from = request.POST["date_from"]
    date_to = request.POST["date_to"]

    day_count = int(date_to[0:2]) - int(date_from[0:2])

    #print(Day.objects.filter(date=date_from))
    query_date = int(date_from[0:2])

    #days correspond to data
    raw_data = []

    if(len(Day.objects.filter(date=date_from)) == 0):
        raw_data.append([{'date': date_from, 'gluten': 0, 'dairy': 0, 'sugar': 0, 'nausea': 0, 'fatigue': 2, 'bloated': 0}])
    else:
        raw_data.append(list(Day.objects.filter(date=date_from).values('date','gluten', 'dairy','sugar', 'nausea', 'fatigue', 'bloated')))

    for data in range(0, day_count):
            query_date += 1

            if len(str(query_date)) < 2:
                query_date = "0"+str(query_date)
                    
            if len(Day.objects.filter(date=str(query_date) + str(date_from[2:]))) == 0:
                print("activated")
                raw_data.append([{'date': str(query_date) + str(date_from[2:]), 'gluten': 0, 'dairy': 0, 'sugar': 0, 'nausea': 0, 'fatigue': 0, 'bloated': 0}])
            else:
                raw_data.append(list(Day.objects.filter(date=str(query_date) + str(date_from[2:])).values('date','gluten', 'dairy','sugar', 'nausea', 'fatigue', 'bloated')))

            query_date = int(query_date)
                
    # bar chart data
    b_chart_averages = []

    avgdairy = 0
    avggluten = 0
    avgsugar = 0
    avgnausea = 0
    avgfatigue = 0
    avgbloating = 0

    dairy_ds = []
    gluten_ds = []
    sugar_ds = []
    nausea_ds = []
    fatigue_ds = []
    bloating_ds = []

    days = []
    for day in raw_data:
        days.append(str(day[0]['date'][0:2]) + "/" + str(day[0]['date'][2:4]) + "/" + str(12))
        avgdairy += day[0]['dairy']
        avggluten += day[0]['gluten']
        avgsugar += day[0]['sugar']
        avgnausea += day[0]['nausea']
        avgfatigue += day[0]['fatigue']
        avgbloating += day[0]['bloated']

        dairy_ds.append(day[0]['dairy'])
        gluten_ds.append(day[0]['gluten'])
        sugar_ds.append(day[0]['sugar'])
        nausea_ds.append(day[0]['nausea'])
        fatigue_ds.append(day[0]['fatigue'])
        bloating_ds.append(day[0]['bloated'])



    b_chart_averages.append(round(avgdairy / day_count, 2))
    b_chart_averages.append(round(avggluten / day_count, 2))
    b_chart_averages.append(round(avgsugar / day_count, 2))
    b_chart_averages.append(round(avgnausea / day_count, 2))
    b_chart_averages.append(round(avgfatigue / day_count, 2))
    b_chart_averages.append(round(avgbloating / day_count, 2))

    context_dict = {}
    context_dict['b_chart_avgdairy'] = b_chart_averages[0]
    context_dict['b_chart_avggluten'] = b_chart_averages[1]
    context_dict['b_chart_avgsugar'] = b_chart_averages[2]
    context_dict['b_chart_avgnausea'] = b_chart_averages[3]
    context_dict['b_chart_avgfatigue'] = b_chart_averages[4]
    context_dict['b_chart_avgbloated'] = b_chart_averages[5]

    context_dict['p_chart_totaldairy'] = avgdairy
    context_dict['p_chart_totalgluten'] = avggluten
    context_dict['p_chart_totalsugar'] = avgsugar
    context_dict['p_chart_totalnausea'] = avgnausea
    context_dict['p_chart_totalfatigue'] = avgfatigue
    context_dict['p_chart_totalbloating'] = avgbloating

    context_dict['l_chart_dairy'] = json.dumps(dairy_ds)
    context_dict['l_chart_gluten'] = json.dumps(gluten_ds)
    context_dict['l_chart_sugar'] = json.dumps(sugar_ds)
    context_dict['l_chart_nausea'] = json.dumps(nausea_ds)
    context_dict['l_chart_fatigue'] = json.dumps(fatigue_ds)
    context_dict['l_chart_bloating'] = json.dumps(bloating_ds)

    nausea_scatter_dairy = []
    nausea_scatter_gluten = []
    nausea_scatter_sugar = []

    fatigue_scatter_dairy = []
    fatigue_scatter_gluten = []
    fatigue_scatter_sugar = []

    bloating_scatter_dairy = []
    bloating_scatter_gluten = []
    bloating_scatter_sugar = []


    # nausea scatter
    for day in raw_data:
        if day[0]['nausea'] > 0:
            if day[0]['dairy'] > 0:
                nausea_scatter_dairy.append([day[0]['nausea'], day[0]['dairy']])
                
            if day[0]['gluten'] > 0:
                nausea_scatter_gluten.append([day[0]['nausea'], day[0]['gluten']])
            
            if day[0]['sugar'] > 0:
                nausea_scatter_sugar.append([day[0]['nausea'], day[0]['sugar']])

        if day[0]['fatigue'] > 0:
            if day[0]['dairy'] > 0:
                fatigue_scatter_dairy.append([day[0]['fatigue'], day[0]['dairy']])
            
            if day[0]['gluten'] > 0:
                fatigue_scatter_gluten.append([day[0]['fatigue'], day[0]['gluten']])
            
            if day[0]['sugar'] > 0:
                fatigue_scatter_sugar.append([day[0]['fatigue'], day[0]['sugar']])
        
        if day[0]['bloated'] > 0:
            if day[0]['dairy'] > 0:
                bloating_scatter_sugar.append([day[0]['bloated'], day[0]['dairy']])
            
            if day[0]['gluten'] > 0:
                bloating_scatter_sugar.append([day[0]['bloated'], day[0]['gluten']])
            
            if day[0]['sugar'] > 0:
                bloating_scatter_sugar.append([day[0]['bloated'], day[0]['sugar']])


    context_dict['dates'] = json.dumps(days)

    context_dict['nausea_scatter_dairy'] = nausea_scatter_dairy
    context_dict['nausea_scatter_gluten'] = nausea_scatter_gluten
    context_dict['nausea_scatter_sugar'] = nausea_scatter_sugar

    context_dict['fatigue_scatter_dairy'] = fatigue_scatter_dairy
    context_dict['fatigue_scatter_gluten'] = fatigue_scatter_gluten
    context_dict['fatigue_scatter_sugar'] = fatigue_scatter_sugar

    context_dict['bloating_scatter_dairy'] = bloating_scatter_dairy
    context_dict['bloating_scatter_gluten'] = bloating_scatter_gluten
    context_dict['bloating_scatter_sugar'] = bloating_scatter_sugar

    context_dict['display'] = ""

    
    return render(request, 'stats.html', context_dict)

def save_data(request):
    print("test")
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