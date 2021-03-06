from django.shortcuts import (
    render , HttpResponse ,
    redirect , Http404 )
from django.contrib.auth.decorators import user_passes_test ,login_required 
from Authentication.models import User ,UserManager
from .models import Seller
from Customer.models import Order
from product.models import Product
from .forms import SellerRegistrationForm , SellerForm , ProductForm

def is_user_seller(user):
    if user.user_type=="SELLER" and user.is_active:
        return True

@login_required(login_url="signin")
@user_passes_test(is_user_seller , login_url='signin')
def seller_home(request):
    try:
        seller =  Seller.objects.get(user=request.user)
    except User.DoesNotExist:
        raise Http404("Seller Does Not Exisit")
    
    sellerproducts = Product.objects.filter(seller=seller)
    totalsellerproducts = sellerproducts.count()
    context = {'seller':seller,'sellerproducts':sellerproducts,"totalsellerproducts":totalsellerproducts }
    return render(request,"seller_home.html",context)

 
def seller_register(request):
    if request.method == "POST":
        form = SellerRegistrationForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            seller =  Seller.objects.get(user__email=email)
            return redirect('signin')
    
    form = SellerRegistrationForm()
    context = {'form':form}
    return render(request,'seller_register.html' ,context )

@login_required(login_url="signin")
@user_passes_test(is_user_seller , login_url='signin')    
def settings_seller(request ):
    seller =  Seller.objects.get(user=request.user)
    form =  SellerForm(instance=seller)
    if request.method == 'POST':
        form = SellerForm(request.POST,request.FILES,instance=seller)
        if form.is_valid():
            form.save()    
            
    context = {'form' : form ,"seller":seller}
    

    return render(request , 'settings_update_seller.html' , context)

@login_required(login_url="signin")
@user_passes_test(is_user_seller , login_url='signin')
def place_product(request ):
    seller =  Seller.objects.get(user=request.user)
    form = ProductForm(initial={'seller':seller})
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller-home' , pk=pk)
    context = {'form' :  form ,}
    return render(request,'place_Product.html' , context)

@login_required(login_url="signin")
@user_passes_test(is_user_seller , login_url='signin')
def update_product(request ,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method =="POST":
        form = ProductForm(request.POST , instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller-home' , pk=seller.id)
    context = {'form' :  form ,}
    return render(request,'place_Product.html' , context)    

@login_required(login_url="signin")
@user_passes_test(is_user_seller , login_url='signin')
def seller_orders_view (request, pk):
    seller = Seller.objects.get(id=pk)
    order =Order.objects.filter(product__seller__id=pk)
    context ={"order":order}
    return render(request,'orders.html' , context)
