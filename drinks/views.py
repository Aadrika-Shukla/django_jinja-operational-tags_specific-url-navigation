from django.shortcuts import render

# Create your views here.
def blue_lagoon(request):
    return  render(request,'blue_lagoon.html')

def orange_punch(request):
    return render(request,'orange_punch.html')
