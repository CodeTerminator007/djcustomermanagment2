from django.shortcuts import (
    render , HttpResponse ,
    redirect , Http404 )
    
from Authentication.models import User ,UserManager
from .models import Seller
from product.models import Product
from .forms import SellerRegistrationForm


def seller_home(request,pk):
    try:
        seller =  Seller.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404("Seller Does Not Exisit")
    
    sellerproducts = Product.objects.filter(seller=seller)
    totalsellerproducts = sellerproducts.count()
    context = {'seller':seller,'sellerproducts':sellerproducts,"totalsellerproducts":totalsellerproducts }
    return render(request,"seller_home.html",context)


def seller_register(request):
    if request.method == "POST":
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            seller =  Seller.objects.get(user__email=email)
            return redirect('seller-home',seller.id)
        else:
            return HttpResponse("Error in in Form is  Not Valid")
    form = SellerRegistrationForm()
    context = {'form':form}
    return render(request,'seller_register.html' ,context )
