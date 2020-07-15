
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('About', views.about, name='about'),
    path('analyze', views.analyze, name='analyze'),
    url(r'^employe',views.employeeList.as_view()),
    #path('ex1', views.ex1, name='ex1'),


]
