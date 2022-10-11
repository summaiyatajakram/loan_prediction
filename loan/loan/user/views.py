from django.shortcuts import render,redirect
from django.contrib.auth.models import user
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
if request.method=="POST":
        fname=request.POST['Fname']
        mname=request.POST['Mname']
        Uname=request.POST['Uname']
        phone=request.POST['phone number']
        citizen=request.POST['citizen']
        Email=request.POST['Email']
        date=request.POST['date of birth']
        address=request.POST['address']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password==confirmpassword:
            if register.objects.filter(username=fname).exists():
                messages.info(request,"Username exist")
                return render(request,'s.html')
            elif  register.objects.filter(Email=Email).exists():
                  messages.info(request,"Email available")
                  return render(request,'register.html')
            else:     
        
                #to create data in db tables
                #create object for user
                user=register.objects.create_user(fname=fname,mname=mname,phone_number=phone,Uname=Uname,
                citizen=citizen,Email=Email,password=password,confirmpassword=confirmpassword,address=address).save()
                return(request,'login.html')
        else:
            messages.info(request,"Password Not matching")
            return render(request,"register.html")
else:
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(uname=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"home.html")
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'login.html')
    else:   
        return render(request,'login.html')
