from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name= 'create'),
    path('myprofile', views.myprofile, name='myprofile'),
    # path('',views.home, name='home')
]

