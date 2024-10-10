from .views import  calculate
from django.urls import path

urlpatterns=[
    path("calculate/", calculate, name="calculate")
]