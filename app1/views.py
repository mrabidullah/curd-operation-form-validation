from django.shortcuts import render,HttpResponse,redirect
from app1.models import student,principle
from .models import Teachers
from django.contrib import messages


# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth .decorators import login_required
#________user Messages______________________________>>>>>>>
from django.contrib import messages
from abid1.forms import PrincipalMessageForm

# from .models import user

def signupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        a="Confirm password is not the same. Try again"
        if pass1!=pass2:
           
            return render(request,'signup.html',{ 'a':a })
        
        else:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def loginPage(request):
    a="username or password is incorrect!"
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'a':a})
            
    return render(request,'login.html')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def logoutPage(request):
    logout(request)
    return redirect('login')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@login_required(login_url='login')


def home(request):
    return render(request,'dash.html')


@login_required(login_url='login')
def form(request):
    if request.method == "POST":
        name=request.POST.get("name")
        F_name=request.POST.get("F_name")
        dep_name=request.POST.get("dep_name")
        Roll_number=request.POST.get("Roll_number")
        address=request.POST.get("address")
        email=request.POST.get("email")
        marks=request.POST.get("marks") 
        rec=student(
            name = name,
            F_name = F_name,
            dep_name = dep_name,
            Roll_number = Roll_number,
            address = address,
            email = email,
            marks = marks,
        )
        rec.save()
        return redirect('home')
    return render(request,'form.html')

@login_required(login_url='login')
def table(request):
    rec1=student.objects.all()
    rec2={
        'rec1' : rec1,
    }

    return render(request,'table.html',rec2)

def update (request,id):
    i = student.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        F_name=request.POST.get("F_name")
        dep_name=request.POST.get("dep_name")
        Roll_number=request.POST.get("Roll_number")
        address=request.POST.get("address")
        email = request.POST.get("email") 
        marks=request.POST.get("marks")
        
        rec= student( 
            id = id, 
            name =  name,
            F_name = F_name,
            dep_name = dep_name,
            Roll_number = Roll_number,
            address = address,
            email = email,
            marks = marks,
        )
        rec.save()
        # return redirect('')
        return redirect('table')
    return render(request,"update.html",{'i' : i})
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def delete(request,id):
    i=student.objects.filter(id = id ).delete()
    
    delete = {
        'i' : i
    }
    return redirect('table')
        
    
    
    
    
#>>>>>>>>>>>>>principle>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def princi(request):
    return render (request,'principle.html')




def aboutprincipal(request):
    return render(request,'only_principal.html')







#>>>>>>>>>>>>>>>>>>>>>>>>messages>>>>>>>>>>>>>>>>>>>>>>>>>>>



# def principal_view(request):
#     if request.method == "POST":
#         form = PrincipalMessageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your message has been sent successfully!")
#             return redirect('principle')  # Redirect to same page after success
#     else:
#         form = PrincipalMessageForm()
#     return render(request, "principal_form.html", {"form": form})

















#>>>>>>>>>>>>>>>>>>>>>>> for reply >>>>>>>>>>>>>>>>>>>>>>
from django.core.mail import send_mail




def principal_view(request):
    form=''
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        Txt_msg=request.POST.get('message')
        
        data=PrincipalMessageForm(
            name = name,
            email = email,
            subject = subject,
            Txt_msg = Txt_msg,
        )
        data.save()
        form='data insert'
        return HttpResponse("your message scuessfull send:")
    return render(request,'principal_form.html',{'form':form})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Teachers >>>>>>>>>>>>>>>>>>>>>

def cant_teacher(request):
    if request. method == "POST":
        name=request.POST.get('name')
        f_name=request.POST.get('f_name')
        P_number=request.POST.get('P_number')
        email=request.POST.get('email')
        address=request.POST.get('address')
        message=request.POST.get('message')
        
        trc= Teachers(
                name = name,
                f_name = f_name,
                P_number = P_number,
                email = email,
                address = address ,
                message = message,
          )   
        trc.save()
        return redirect('T_table')
    return render(request,'T_form.html')
        
        
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>T_table >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def T_table(request):
    trc=Teachers.objects.all()
    trc2={
          'trc':trc,
           }
    
    return render(request,'T_table.html',trc2) 
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Updata >>>>>>>>>>>>>>>>>>>>>>>>>
def up_teacher(request,id):
    i =Teachers.objects.get(id=id)
    if request.method == "POST":
        name=request.POST.get('name')
        f_name=request.POST.get('f_name')
        P_number=request.POST.get('P_number')
        email=request.POST.get('email')
        address=request.POST.get('address')
        message=request.POST.get('message')
        
        trc=Teachers(
            id = id ,
          name = name,
          f_name = f_name,
          P_number = P_number,
          email = email,
          address = address,
          message = message,
         )   
        trc.save()
        return redirect('T_table',)
    return render(request,'U_form.html',{'i':i})
        
def T_delete(request,id):
    j=Teachers.objects.filter(id=id).delete()
    T_delete = { 
        'j':j
    }
    return redirect('T_table')