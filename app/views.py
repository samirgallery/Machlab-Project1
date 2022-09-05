
from django.core.checks import messages
from django.shortcuts import render
from.models import*
# Create your views here.

#vies for register page 
def RegisterPage(request):
    return render(request,"app/register.html")

#View for user registation 
def UserRegister(request):
    if request.method =="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        #first we will validate that user alrady exsit
        user=User.objects.filter(Email=email)
        

        if user:
            messages ="user all ready exits "
            return render (request,"app/register.html",{'msg':messages})
        
        else:
            if password == cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                messages="User register  Successfully "
                return render(request,"app/login.html",{'msg':messages})
            else:
                messages="password and confirm password does not match "
                pass
                # (request,"app /register.html",{'msg':messages})


#LOgin View

def LoginPage(request):
    return render(request,"app/login.html")


#Login User\
def LoginUser(request):
    if request.method == "POST":
        email=request.POST ['email']
        password=request.POST['password']

        #Cheking the email with database 
        user = User.objects.get(Email=email)
        if user : # we are getting user data in session 
            if user.Password == password:
                request.session['Firstname'] =user.Firstname
                request.session['Lastname']= user.Lastname
                request.session ['Email']=user.Email

                return render(request,"app/home.html")
            else:
                messages="password does nort match "
                return render(request,"app/login.html",{'msg':messages})

        else:
            messages="User does not exist"
            return render(request,"app/register.html",{'msg':messages})
            #Login view
def LoginPage(request):
    return render(request,"app/login.html")
#login user
def LoginUser(request):
    if request.method == "POST":
        email=request.POST ['email']
        password=request.POST['password']

        #Cheking tghe email id with database 
        user=User.objects.get(Email=email)

        if user:
            #We are getting user data in session 
            if user.Password == password:
                request.session ['Firstname']=user.Firstname
                request.session ['Lastname']=user.Lastname
                request.session ['Email']=user.Email
                return render(request,"app/home.html")
            else:
                messages="Password does not match"
                return render(request,"app/login.html",{'msg':messages})
        else:
            messages="User Dost not Exist"
            return render (request,"app/register.html",{'msg':messages})


