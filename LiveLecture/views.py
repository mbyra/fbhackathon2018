from .models import User
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import datetime, timedelta

def index(request):
    context = {}
    return render(request, 'LiveLecture/base.html', context)
