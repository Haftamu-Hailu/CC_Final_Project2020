from django.urls import path

from form import views

app_name = 'form'

urlpatterns = [
    path('', views.home, name='home'),
    path('setup', views.simulatorSetUp, name='simulatorSetUp'),
]
