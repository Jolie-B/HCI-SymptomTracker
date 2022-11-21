from django import forms
from django.forms import ModelForm
from django.db.models.expressions import Value
from tracker.models import *
from django.contrib.auth.models import User


class DayForm(ModelForm):
    date = forms.CharField()

    #symptoms
    fatigue = forms.IntegerField()
    nausea = forms.IntegerField()
    bloated = forms.IntegerField()

    #foods
    dairy = forms.IntegerField()
    gluten = forms.IntegerField()
    sugar = forms.IntegerField()
    
    class Meta:
        model = Day
        fields = ('date', 'fatigue', 'nausea', 'bloated', 'dairy', 'gluten', 'sugar',)

