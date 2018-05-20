from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST

from .models import User, Lecture, Subscription, Messages
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import datetime, timedelta

def index(request,listAll=False):
    template = loader.get_template('LiveLecture/upcoming.html')
    if not request.user.is_anonymous:
        print(type(request.user))
        lecture_list =get_user_courses(request.user)
    else:
        lecture_list=None
    signInDisable=False
    if lecture_list is None:
        lecture_list = Lecture.objects.all()
    elif listAll:
        lecture_list=get_user_courses(request.user,True)
    else:
        signInDisable=True
    context = {'lecture_list' : lecture_list,'signInEnable' : signInDisable}
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
        lecture_list = get_user_courses(user)
        context = {'login_success': login_success,'lecture_list': lecture_list}
        return render(request, 'LiveLecture/upcoming.html', context)
    else:
        print("uzytkownik nie istnieje")
        login_failure = True
        context = {'login_failure': login_failure}
        return render(request, 'LiveLecture/upcoming.html', context)

def lecture(request, pk):
    template = loader.get_template('LiveLecture/lecture.html')
    lecture = Lecture.objects.filter(pk=pk)[0]
    if lecture is None:
        raise ValueError("There is no lecture with this pk!")

    substriptions = Subscription.objects.filter(lecture=lecture)
    students = []
    for substription in substriptions:
        students.append(substription.student)

    messages = Messages.objects.filter(lecture=lecture).order_by('-likes')

    context = {'lecture': lecture, 'students': students, 'messages' : messages}
    return render(request, 'LiveLecture/lecture.html', context)


def add_message(request, pk):
    if 'message' not in request.POST:
        raise ValidationError("No message in POST")

    print(request.POST['message'])

    template = loader.get_template('LiveLecture/lecture.html')
    lecture = Lecture.objects.filter(pk=pk)[0]
    if lecture is None:
        raise ValueError("There is no lecture with this pk!")

    substriptions = Subscription.objects.filter(lecture=lecture)
    students = []
    for substription in substriptions:
        students.append(substription.student)

    Messages.objects.create(lecture=lecture, student=request.user, content=request.POST['message'], likes=0)

    messages = Messages.objects.filter(lecture=lecture).order_by('-likes')

    context = {'lecture': lecture, 'students': students, 'messages' : messages}

    return render(request, 'LiveLecture/lecture.html', context)

def add_like(request, lecture_pk, message_pk):
    message = Messages.objects.get(pk=message_pk)
    message.likes += 1
    message.save()
    lecture = Lecture.objects.filter(pk=lecture_pk)[0]

    substriptions = Subscription.objects.filter(lecture=lecture)
    students = []
    for substription in substriptions:
        students.append(substription.student)

    messages = Messages.objects.filter(lecture=lecture).order_by('-likes')

    context = {'lecture': lecture, 'students': students, 'messages' : messages}

    return render(request, 'LiveLecture/lecture.html', context)

def modify_timeline(request):
    messages = Messages.objects.filter(lecture=lecture).order_by('-likes')

    context = {'lecture': lecture, 'students': students, 'messages' : messages}

    return render(request, 'LiveLecture/lecture.html', context)
def add_subscriptions(request,lecture):
    Subscription.objects.create(lecture=Lecture.objects.get(pk=lecture),student=request.user)
    print("hello")
    index(request,False)

def get_user_courses(user,invert=False):
    subscription_list = Subscription.objects.filter(student=user)
    lecture_list=[]
    for subscription in subscription_list:
        lecture_list.append(subscription.lecture)
    if invert:
        lecture_list=[x for x in Lecture.objects.all() if x not in lecture_list]

    return lecture_list