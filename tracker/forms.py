from django import forms
from django.forms import ModelForm
from django.db.models.expressions import Value
from tracker.models import *
from django.contrib.auth.models import User

class DayForm(ModelForm):
    date = forms.DateField(widget=forms.HiddenInput(), required=False)

    #symptoms
    fatigue = forms.IntegerField()
    nausea = forms.IntegerField()
    bloated = forms.IntegerField()

    #foods
    dairy = forms.IntegerField()
    gluten = forms.IntegerField()
    sugar = forms.IntegerField()

    daySlug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Day
        fields = ('fatigue', 'nausea', 'bloated', 'dairy', 'gluten', 'sugar',)


class ArticleForm(ModelForm):
    class Meta:
        model = Day
        fields = ['date',]