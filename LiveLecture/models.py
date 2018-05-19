from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import timedelta
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_lecturer = models.NullBooleanField()

    def __str__(self):
        return 'User %s %s, lecturer: %s' % (self.first_name, self.last_name, self.is_lecturer)

class Lecture(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    max_students = models.IntegerField()

    def __str__(self):
        return 'Lecture: %s' % self.name

class Subscription(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return 'Substription of %s to lecture: %s' % (self.student, self.lecture)


