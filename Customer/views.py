from django.shortcuts import render , HttpResponse , redirect
from Authentication.models import *
from .forms import CustomerRegistrationForm
def home(request):
    context = {}
    return render(request,"home.html",context)


def register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            sucess = "User has Been Created"
            context = {'sucess':sucess}
            return render(request,'home.html',context)
        else:
            return HttpResponse("Error in in Form is  Not Valid")
    form = CustomerRegistrationForm()
    context = {'form':form}
    return render(request,'register.html' ,context )
