from django.urls import path

from . import views

app_name = 'LiveLecture'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('login_or_register/', views.login_or_register, name='login_or_register'),
    path('lecture/<int:pk>',views.lecture, name='lecture')
]