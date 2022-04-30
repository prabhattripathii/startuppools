from django.shortcuts import render

# Create your views here.

def ServiceFun(request):
    return render(request,'service.html')