from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from proapp.models import Ownerreg,Buyerreg,Property,Brqst,Purchase

from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.db.models.functions import Coalesce
from django.db.models import Max, Value
from datetime import date
from . forms import *
from . models import *
from django.db.models import Q



class Addowner(CreateView):
    template_name = "add_owner.html"
    form_class = Ownerform
    success_url = "/"

def home(request):
    all=Property.objects.all()
    context={'prop':all}
    return render(request,"home.html",context)


def property_search(request):
    if request.method == 'GET':
        ptype = request.GET.get('ptype')
        district = request.GET.get('district')
        
        # Filter properties based on ptype and district (case-insensitive)
        properties = Property.objects.filter(Q(ptype__icontains=ptype) & Q(district__icontains=district))
        
        context = {
            'prop': properties
        }
        
        return render(request, 'search.html', context)
    
def all(request):
    p=Property.objects.all()
    context={'properties':p}
    return render(request,'all-property.html',context)

def buyerreg_view(request):
    if request.method == 'POST':
        form = BuyerregForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/login/')  
    else:
        form = BuyerregForm()

    return render(request, 'add_buyer.html', {'form': form})

def ownerreg_view(request):
    if request.method == 'POST':
        form = Ownerform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/login/')  
    else:
        form = Ownerform()

    return render(request, 'add_owner.html', {'form': form})

def ownerhome(request):
    return render(request,'owner_home.html')

def login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pwd = request.POST.get('password')

        ul = Buyerreg.objects.filter(username=un, password=pwd)
        ol= Ownerreg.objects.filter(username=un,password=pwd).first()
        print(ul)
       
        #user_type = userlogin.objects.filter(user_type = 'user')
        if ol:
            if ol.is_verified == True:
                request.session['user_name'] = ol.username
                request.session['user_id'] = ol.oid
                return redirect("http://127.0.0.1:8000/owner_home")
            else:
                context ={ 'msg1':'Admin NOt Yet Approved...!'}
                return render(request, 'login.html',context)
        
        if ul:
            request.session['user_name'] = ul[0].username
            request.session['user_id'] = ul[0].bid
            return redirect("/")

        
        else:
            context ={ 'msg1':'Invalid username and password...!'}
            return render(request, 'login.html',context)

    else:
        return render(request, 'login.html')
    


def prop_detail(request,id):
    
    property = get_object_or_404(Property, pid=id)

    if request.method == "POST":
        date=request.POST["date"]
        uid=request.session['user_id']
        user=Buyerreg.objects.get(bid=uid)
        owner=property.user
        new=Book.objects.create(prop=property,user=user,owner=owner,status="Booked",app_date=date)
        new.save()
        return redirect("/")
    else:
        return render(request, 'prop-detail.html', {'property': property})
   

def book(request,pk):
    prop=Property.objects.get(pid=pk)
    uid=request.session['user_id']
    user=Buyerreg.objects.get(bid=uid)
    owner=prop.user
    new=Book.objects.create(prop=prop,user=user,owner=owner,status="Booked")
    new.save()
    return redirect("/")

    
def logout(request):

    try:
        del request.session['user_name']

        del request.session['user_id']
    except:
         return redirect("/")
    else:
        return redirect("/")
def add(request):
    context = {}  # Define the context variable
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            uid = request.session["user_id"]
            user = Ownerreg.objects.get(oid=uid)
            p.user = user
            p.save()
            return redirect('http://127.0.0.1:8000/my/')  # Redirect to a success page after form submission
    else:
        form = PropertyForm()
        context['form'] = form  # Assign the form to the context variable
    
    return render(request, 'add_property.html', context)

def myprop(request):
    uid = request.session["user_id"]
    user =Ownerreg.objects.get(oid=uid)
    a=Property.objects.filter(user=user)
    context={'a':a}
    return render(request,'list_property.html',context)

def delete(request,pk):
    d=Property.objects.get(pid=pk)
    d.delete()
    return redirect("/my/")

def requests(request):
    o=request.session['user_id']
    owner=Ownerreg.objects.get(oid=o)
    boo=Book.objects.filter(owner=owner)
    return render(request,'res.html',{'a':boo})

def mybook(request):
    u=request.session['user_id']
    user=Buyerreg.objects.get(bid=u)
    boo=Book.objects.filter(user=user)
    return render(request,'my_booking.html',{'a':boo})

def approve_booking(request, pk):
    try:
        booking = Book.objects.get(id=pk)
        booking.status="Approved"
        booking.save()
        # Perform necessary operations to approve the booking
        # For example, update the status field or send a notification
        
        # Redirect to the page where the bookings are displayed
        return redirect('http://127.0.0.1:8000/req/')
    except Book.DoesNotExist:
        # Handle the case when the booking doesn't exist
        # Display an error message or redirect to an error page
        pass

def reject_booking(request, pk):
    try:
        booking = Book.objects.get(id=pk)
        booking.status="Rejected"
        booking.save()
        # Perform necessary operations to reject the booking
        # For example, update the status field or send a notification
        
        # Redirect to the page where the bookings are displayed
        return redirect('http://127.0.0.1:8000/req/')
    except Book.DoesNotExist:
        # Handle the case when the booking doesn't exist
        # Display an error message or redirect to an error page
        pass





#extra
