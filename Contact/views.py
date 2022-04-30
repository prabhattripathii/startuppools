from django.shortcuts import redirect, render

from .models import *

# Create your views here.
def ContactPageFun(request):
    return render(request, "contact.html")


def MessageSendingFun(request):
    if request.method == "POST":
        sendernamedb = request.POST['sendername']
        sendermaildb = request.POST['sendermail']
        sendersubjectdb = request.POST['sendersubject']
        sendermessagedb = request.POST['sendermessage']
        Updatedb = ModelForMessages.objects.create(Sendername = sendernamedb, Sendermail = sendermaildb, Sendersub = sendersubjectdb, Sendermess = sendermessagedb)
        redirect('/contact')