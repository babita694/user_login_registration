from django.shortcuts import render,redirect
from .models import*
#def signup(request):
 #return render(request, 'app/signup.html')

def signup(request):
    if request.method =="POST":
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        cpassword= request.POST['cpassword']
       
       
        user=User.objects.filter(Email=email)
       
        if user:
           message="user already exit"
           return render (request,"app/signin.html",{'msg':message})
        else:
            if password==cpassword :
                newuser =User.objects.create(username=username ,email=email,password=password,cpassword=cpassword)
                
                message= "User register successfully "
                return render(request,"app/home.html",{'msg':message})
            else:
                message="password and confirmpassword doesnt match"
                return render(request,"app/signup.html",{'msg':message})
            
            
    return render(request, 'app/signup.html')        
    

def home(request):
   return render(request, 'app/home.html')


def signin(request):
 return render(request, 'app/signin.html')
             
            
        
        
        
 