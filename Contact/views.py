from django.shortcuts import render

# Create your views here.
def ContactPageFun(request):
    return render(request, "contact.html")