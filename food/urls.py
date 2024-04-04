from django.urls import path 
from food.views import *
app_name='food'
urlpatterns=[
    path('panipuri/',panipuri,name='panipuri'),
    path('kajukatli/',kajukatli,name='kajukatli'),
]