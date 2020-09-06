from django.shortcuts import render , HttpResponse , redirect , Http404 
from Authentication.models import User ,UserManager
from .models import Customer
from django.contrib.auth import authenticate , login , logout
from .forms import CustomerRegistrationForm

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        print(user.user_type)
        
        if user is not None :            
            login(request,user)
            if user.user_type == "CUSTOMER":
                customer =  Customer.objects.get(user__email=user.email)
                return redirect('customer-page' , customer.id)
            else:
                pass               
        else:
            pass
    return render(request , 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')
def customerpage(request,pk):
    try:
        customer =  Customer.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404("User Does Not Exisit")

    context = {'customer':customer}
    return render(request,"customer.html",context)


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
