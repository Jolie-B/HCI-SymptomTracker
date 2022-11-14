import os
import string
import random
import csv


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'symptomTracker.settings')

import django

django.setup()
from django.core.files import File
from django.db.models import Q
from tracker.models import *
from datetime import date
from django.contrib.auth.models import User


def populate():

    # Day Populate
    
    dayinfo = [
        {
            'date': date(2020, 11, 19),   
            'fatigue': 0,
            'nausea': 0,
            'bloated': 0,
            'dairy': 5,
            'gluten': 0,
            'sugar': 0,
        },

        {
            'date': date(2020, 11, 20),   
            'fatigue': 0,
            'nausea': 3,
            'bloated': 0,
            'dairy': 0,
            'gluten': 3,
            'sugar': 0,
        },

        {
            'date': date(2020, 11, 21),   
            'fatigue': 0,
            'nausea': 0,
            'bloated': 0,
            'dairy':3,
            'gluten': 3,
            'sugar': 3,
        },

        {
            'date': date(2020, 11, 22),   
            'fatigue': 1,
            'nausea': 2,
            'bloated': 3,
            'dairy': 3,
            'gluten': 4,
            'sugar': 5,
        }
    ]
    Day = []
    for day in dayinfo:
        d= add_day(day['date'], day['fatigue'], day['nausea'], day['bloated'], day['dairy'], day['gluten'], day['sugar'] )
        Day.append(d)

# Model Helper Functions

def add_day(date,fatigue, nausea, bloated, dairy, gluten, sugar):
    d = day.objects.get_or_create(date=date, fatigue=fatigue, nausea=nausea, bloated=bloated, dairy=dairy, gluten=gluten, sugar=sugar)[0]
    d.date = date
    d.fatigue = fatigue
    d.nausea = nausea
    d.bloated = bloated
    d.dairy = dairy
    d.gluten = gluten
    d.sugar = sugar
    d.save()

    return d


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Completed population script, exiting...')
