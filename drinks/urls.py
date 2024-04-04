from django.urls import path 
from drinks.views import *
app_name='drinks'
urlpatterns=[
    path('blue_lagoon/',blue_lagoon,name='blue_lagoon'),
    path('orange_punch/',orange_punch,name='orange_punch'),
]