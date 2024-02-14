from django.shortcuts import render,redirect
from .models import staff,cust,data
from django.contrib import messages
from.forms import AddCust,DataForm
from django.contrib.auth import logout






def home(request):
    return render(request,'home.html')


#staff functions

def staf_signup(request):

    if request.method=="POST":
       firstname=request.POST.get('firstname')
       lastname=request.POST.get('lastname')
       email=request.POST.get('email')
       phonenumber=request.POST.get('phonenumber')
       department=request.POST.get('department')
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=staff(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,department=department,username=username,password=password)
       user.save()
       messages.success(request, f'customer {user.username} has been approved.')
       return redirect("aprv")
    return render (request,"staff_signup.html")


def approve_staff(request, user_id):
    customer = staff.objects.get(id=user_id)
    customer.is_approved = True
    customer.save()
    messages.success(request, f'User {customer.username} has been approved.')
    return redirect('aprv')  # Redirect to a success page or wherever you want


#view for login html
def login_staff(request):
    return render(request,"staff_login.html") 

# staff function loging
def staff_log(request):   
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr=staff.objects.filter(username=username,password=password)
        if cr:
            user_details=staff.objects.get(username=username,password=password)
            id=user_details.id
            firstname=user_details.firstname
            email=user_details.email
            request.session['id']=id
            request.session['firstname']=firstname
            request.session['email']=email
            return redirect('views')
        else:
            messages.error(request,'username or password not correct')
            return redirect('slog')    
    else:
        return render(request,'views.html')   
    
#page of staff
    
def welcome_staff(request):
    id=request.session['id']
    firstname=request.session['firstname']
    email=request.session['email']
    return render(request,"staffdetails.html",{'id':id,'firstname':firstname,'email':email})    

#coustomer *****************************************************************************************

def user_singnup(request):

    if request.method=="POST":
       firstname=request.POST.get('firstname')
       lastname=request.POST.get('lastname')
       email=request.POST.get('email')
       phonenumber=request.POST.get('phonenumber')
       state=request.POST.get('state')
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=cust(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,state=state,username=username,password=password)
       user.save()
       messages.success(request, f'customer {user.username} has been approved.')
       return redirect("aprv")

    return render(request,"cus_signup.html")

def approve_cust(request, user_id):
    customer = cust.objects.get(id=user_id)
    customer.is_approved = True
    customer.save()
    messages.success(request, f'User {customer.username} has been approved.')
    return redirect('aprv')  # Redirect to a success page or wherever you want


def login_cust(request):
    return render(request,"cust_login.html") 


 
def cust_login(request):   
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr=cust.objects.filter(username=username,password=password)
        if cr:
            user_details=cust.objects.get(username=username,password=password)
            id=user_details.id
            firstname=user_details.firstname
            email=user_details.email
            request.session['id']=id
            request.session['firstname']=firstname
            request.session['email']=email
            return redirect('imv')
        else:
            messages.error(request,'username or password not correct')
            return redirect('cuslog')    
    else:
        return render(request,'views.html')   
    

def welcome_user(request):
    id=request.session['id']
    firstname=request.session['firstname']
    email=request.session['email']
    return render(request,"welcome.html",{'id':id,'firstname':firstname,'email':email})        
  

def aproov(request):
    return render(request,"approve.html" )
#apruval


# table show in customer ****************************************************************************

def views_cust(request):
    cr=cust.objects.all()
    firstname=request.session['firstname']
    email=request.session['email']
    return render (request,"staffdetails.html",{'cm':cr,'firstname':firstname,'email':email}) 
    
def cust_views(request,pk):
    cr=cust.objects.get(id=pk)
    return render(request,"cus_details.html",{'cm':cr}) 

def delete(request,pk):
    cr=cust.objects.get(id=pk)
    cr.delete()
    return redirect("views")

def update_cust(request,pk):     
    cr=cust.objects.get( id=pk)
    form=AddCust(instance=cr)
    if request.method=="POST":
        form=AddCust(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect("views")
    return render(request,"cust_update.html",{'form':form})  


#staff enter details***************************************************************************
def uplode(request):
    form=DataForm()
    if request.method=='POST':
        form=DataForm(request.POST,request.FILES)
        if form.is_valid():
         form.save()
         return redirect("imv")
    return render(request,"new.html",{'form':form})


def image_vw(request):
    cr=data.objects.all()
    return render(request,"welcome.html",{'cm':cr})

# def delete_img(request,pk):
#     cr=data.objects.get(id=pk)
#     cr.delete()
#     return redirect("imv")

def image(request,pk):
    cr=data.objects.get(id=pk)
    return render(request,"book.html",{'cm':cr}) 

def logoutstaf(request):
    logout(request)
    return redirect('slog')

def logoutuser(request):
    logout(request)
    return redirect('cuslog')





















