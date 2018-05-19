from django.views.decorators.http import require_POST

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

def login_view(request):
    context = {}
    return render(request, 'LiveLecture/login.html', context)

@transaction.atomic
@require_POST
def login_or_register(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        print("uzytkownik istnieje")
        login(request, user)
        login_success = True
        context = {'login_success': login_success}
        return render(request, 'LiveLecture/upcoming.html', context)
    else:
        print("uzytkownik nie istnieje")
        login_failure = True
        context = {'login_failure': login_failure}
        return render(request, 'LiveLecture/upcoming.html', context)
def lecture(request):
    template = loader.get_template('LiveLecture/lecture.html')
    context = {}
    return render(request, 'LiveLecture/lecture.html', context)
