from .models import User, Lecture
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import datetime, timedelta

def index(request):
    template = loader.get_template('LiveLecture/upcoming.html')
    lecture_list = Lecture.objects.all()
    context = {'lecture_list' : lecture_list}
    return render(request, 'LiveLecture/upcoming.html', context)

def logout_view(request):
    logout(request)
    context = {}
    return render(request, 'LiveLecture/upcoming.html', context)
