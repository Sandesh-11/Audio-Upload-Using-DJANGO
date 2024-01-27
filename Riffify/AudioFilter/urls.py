from django.contrib import admin
from django.urls import path
from AudioFilter import views


urlpatterns = [
  path('',views.index,name="Audio"),
  path('upload/', views.upload, name='Audio')
  
]



