from django.urls import path
from pos import views

app_name = 'pos'

urlpatterns = [
    path('', views.home, name='home'),
]