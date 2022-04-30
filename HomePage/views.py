from django.shortcuts import render

# Create your views here.
def HomePageFun(request):
    return render(request,'index.html')
