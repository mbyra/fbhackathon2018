from random import choice
from LiveLecture.models import User, Subscription, Lecture

for i in range(100):
    student = choice(User.objects.all())
    lecture = choice(Lecture.objects.all())
    Subscription.objects.create(student=student, lecture=lecture)
