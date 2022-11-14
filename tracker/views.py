from hashlib import new
import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


from tool.models import *
from django.db.models import Sum, F
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout



