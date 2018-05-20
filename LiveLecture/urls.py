from django.urls import path

from . import views

app_name = 'LiveLecture'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/<int:listAll>', views.index, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('login_or_register/', views.login_or_register, name='login_or_register'),
    path('lecture/<int:pk>',views.lecture, name='lecture'),
    path('add_subscriptions/<int:pk>',views.add_subscriptions, name='add_subscriptions'),
    path('add_message/<int:pk>', views.add_message, name='add_message'),
]