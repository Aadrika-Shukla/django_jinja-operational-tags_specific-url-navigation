from django.shortcuts import render

# Create your views here.
def panipuri(request):
    return render(request,'panipuri.html')

def kajukatli(request):
    return render(request,'kajukatli.html')
