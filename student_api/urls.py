from django.urls import path
from .views import *

urlpatterns = [
    path('students/',students,name='student'),#defining the endpoint
    path('student/<int:id>',student,name='student')
]