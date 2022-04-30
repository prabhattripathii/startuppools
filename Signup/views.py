from django.shortcuts import render
from .forms import *

# Create your views here.
def SignupFun(request):
    formtoregister = UserRegistrationForm
    print(formtoregister)
    return render(request, 'signup.html',{'form' :formtoregister})