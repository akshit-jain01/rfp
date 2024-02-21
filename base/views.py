from django.shortcuts import render, redirect

from django.core.mail import send_mail, EmailMessage

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterAdminForm, AddRfpForm, AddCategoryForm, VendorForm
from .models import Vendor, Category, RequestForProposal, Quotes

from django.http import HttpResponse

# Create your views here.

def LoginView(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Vendor.objects.get(email=email)
            if user.active_status == False:
                messages.error(request,'vendor not approved')
                return redirect('login')
        except:
            messages.error(request, 'User doesn\'t exist' )

        
        
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid Login Credentials')
        
    return render(request, 'base/index.html')

def LogoutView(request):
    logout(request)
    return redirect('login')

def RegisterView(request):

    form = VendorForm()
    if request.method == 'POST':
        form = VendorForm(request.POST)
        password = request.POST['password']
        email=request.POST['email']

        
        if Vendor.objects.filter(email=email).exists():
        
            messages.error(request,"user with this email already exists")
        
        if form.is_valid():
            vendor = form.save()
            vendor.set_password(password)
            vendor.is_active=True
            vendor.save()
            return redirect('login')
        
        
    return render(request, 'base/register.html', {'form':form})

def RegisterAdminView(request):

    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        password2 = request.POST['password2']
        email=request.POST['email']


        
        if Vendor.objects.filter(email=email).exists():
            messages.error(request,"user with this email already exists")
            return redirect('registeradmin')
        
        if password != password2:
            messages.error(request,"passwordds don\'t match")
            return redirect('registeradmin')
        
        requestadmin = Vendor.objects.create(
            email=email,
            firstname = firstname,
            lastname = lastname,
            no_of_employees = 0,
            revenue = 0,
            pancard_no = 0,
            gst_no = 0,
            mobile = 0)
        
        requestadmin.set_password(password)
        requestadmin.is_active = True
        requestadmin.is_requestadmin = True
        requestadmin.active_status = True
        requestadmin.save()
        return redirect('login')
    
    return render(request, 'base/registeradmin.html')

def ApproveVendorView(request, pk):
    vendor = Vendor.objects.get(id=pk)

    subject="Vendor Approval email"
    
    msg = EmailMessage(subject, f'<div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2"><div style="margin:50px auto;width:70%;padding:20px 0"><div style="border-bottom:1px solid #eee"><a href="" style="font-size:2em;color: #FFD243;text-decoration:none;font-weight:600">Velocity</a></div><p style="font-size:1.2em">Greetings,</p><p style="font-size:1.2em"> Thank you for creating a vendor account on Velocity. You have been approved to submit your quote to requests.<br><b style="text-align: center;display: block;">Note: OTP is only valid for 5 minutes.</b></p><h2 style="font-size: 1.9em;background: #FFD243;margin: 0 auto;width: max-content;padding: 0 15px;color: #fff;border-radius: 4px;"></h2><p style="font-size:1.2em;">Regards,<br/>Team Swaad</p><hr style="border:none;border-top:1px solid #eee" /><div style="float:right;padding:8px 0;color:#aaa;font-size:1.2em;line-height:1;font-weight:500"><p>Swaad</p><p>Velocity Solutions Sector 63 Noida</p><p>U.P.</p></div></div></div>', 'velocity.info.contact@gmail.com', (vendor.email,))
    msg.content_subtype = "html"
    msg.send()

    vendor.active_status = True
    vendor.save()
        
    return redirect('vendors')


@login_required(login_url='/', redirect_field_name='')
def HomeView(request):
    categories = Category.objects.all()
    # email = request.POST['email']
    # vendor = Vendor.objects.get(email=email)

    context = {'categories':categories}
    return render(request, 'base/dashboard.html',context)

@login_required(login_url='/', redirect_field_name='')
def RFPView(request):

    rfp = RequestForProposal.objects.all()

    context = {'rfps':rfp}

    return render(request, 'base/rfp.html', context)

@login_required(login_url='/', redirect_field_name='')
def VendorView(request):

    vendor = Vendor.objects.all()

    context = {'vendors':vendor}

    return render(request, 'base/vendors.html', context)

@login_required(login_url='/', redirect_field_name='')
def RemoveVendorView(request, pk):

    vendor = Vendor.objects.get(id=pk)

    # if request.method == 'POST':
    vendor.delete()
    return redirect('home')
    

@login_required(login_url='/', redirect_field_name='')
def AddRFPView(request):

    form = AddRfpForm()
    if request.method == 'POST':
        form = AddRfpForm(request.POST)
        if form.is_valid():
            rfp = form.save()
            rfp.save()
            return redirect('rfp')
        else:
            messages.error(request,"Pleaese check the form!!")
    
    return render(request, 'base/addrfp.html', {'form':form})

@login_required(login_url='/', redirect_field_name='')
def RemoveRFPView(request, pk):

    rfp = RequestForProposal.objects.get(id=pk)

    # if request.method == 'POST':
    rfp.delete()
    return redirect('home')

@login_required(login_url='/', redirect_field_name='')
def CategoryView(request):

    categories = Category.objects.all()

    context = {'categories':categories}

    return render(request, 'base/categories.html', context)   

@login_required(login_url='/', redirect_field_name='')
def AddCategoryView(request):
    
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
                category = form.save(commit=False)
                category.save()
                return redirect('categories')
        else:
            messages.error("Pleaese check the form!!")
    
    return render(request, 'base/addcategory.html', {'form':form})     

def ApplyRFPView(request,pk):
    rfp = RequestForProposal.objects.get(id=pk)
    
    if request.method=='POST':
        quote = Quotes.objects.create(
            rfp = rfp,
            vendor = request.user,
            quantity = request.POST['quantity'],
            vendor_price = request.POST['vendor_price'],
            total_cost = int(request.POST['quantity']) * int(request.POST['vendor_price']),
            item_description = request.POST['item_description']
        )
        return redirect('rfp')
    
    return render(request,'base/createquote.html')

def GetQuotesView(request,pk):
    rfp = RequestForProposal.objects.get(id=pk)

    rfp_quotes = rfp.quotes_set.all()

    context = {'quotes':rfp_quotes}

    return render(request, 'base/getquotes.html', context)

def VendorQuotesView(request):
    # vendor = Vendor.objects.get(id=pk)
    vendor = request.user
    vendor_quotes = vendor.quotes_set.all()

    context = {'quotes':vendor_quotes}

    return render(request, 'base/getquotes.html', context)

def GetCategoryRequestsView(request, pk):

    category = Category.objects.get(id=pk)

    rfp = category.category.all()

    # category_requests = category.category_set.all()

    context = {'rfps':rfp}

    return render(request, 'base/rfp.html', context)