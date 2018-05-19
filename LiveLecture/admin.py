from django.contrib import admin

from .models import User, Lecture, Subscription

admin.site.register(Lecture)
admin.site.register(User)
admin.site.register(Subscription)
