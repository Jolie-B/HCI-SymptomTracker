from hashlib import new
import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from tracker.models import *
from django.db.models import Sum, F
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def callendar(request):
    return HttpResponse("Hello, world. You're at the tracker callendar.")


def stats(request):
    return HttpResponse("Hello, world. You're at the tracker stats.")


def day(request, date_slug):
    return HttpResponse("Hello, world. You're at the tracker stats.")

