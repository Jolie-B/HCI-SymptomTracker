#!/usr/bin/env python3

import os
import string
import random
import csv
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'symptomTracker.settings')

import django

django.setup()
from django.core.files import File
from django.db.models import Q
from tracker.models import *
from datetime import date
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def populate():

    # Day Populate
    
    dayinfo = import_days("days.json")

    added_days = []
    for day in dayinfo[0]:
        if day['date'] not in added_days:
            add_day(day['date'], day['fatigue'], day['nausea'], day['bloated'], day['dairy'], day['gluten'], day['sugar'])
            added_days.append(day["date"])

# Model Helper Functions

def add_day(date,fatigue, nausea, bloated, dairy, gluten, sugar):
    try:
        d = Day.objects.get_or_create(date=date, fatigue=fatigue, nausea=nausea, bloated=bloated, dairy=dairy, gluten=gluten, sugar=sugar)[0]
    except IntegrityError:
        d = Day.objects.get(date=date)
      
    d.date = date
    d.fatigue = fatigue
    d.nausea = nausea
    d.bloated = bloated
    d.dairy = dairy
    d.gluten = gluten
    d.sugar = sugar

    d.save()
    return d

def import_days(filename):
    days = []

    with open(filename, 'r') as file:
        data = json.load(file)
        for item in data:
            day = {}
            day['date'] = data[item]['date']
            day['fatigue'] = data[item]['fatigue']
            day['dairy'] = data[item]['dairy']
            day['nausea'] = data[item]['nausea']
            day['sugar'] = data[item]['sugar']
            day['gluten'] = data[item]['gluten']
            day['bloated'] = data[item]['bloated']
            days.append(str(day[0:2]) + "/" + str(day[2:4]) + "/" str(day[4:]))

    return days,


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Completed population script, exiting...')
