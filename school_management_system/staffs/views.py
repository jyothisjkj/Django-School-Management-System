from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import Template,Context
from django.contrib.auth.decorators import login_required
from .models import Student,std_messages

#global variables
selected_class = None

# Create your views here.
@login_required(login_url='staff-login')
def staff_loginpage(request):



    # all_students = Student.objects.all()
    all_students=all_students = Student.objects.all()

    
    if request.method == "POST":

        form_type1 = request.POST.get("form_type1")
        form_type2 = "abcd"


        # For the class selection form 
        if form_type1 =="form1":
            global selected_class
            selected_class = request.POST.get("selected_class")
            print("the selection is: ",selected_class)
            if selected_class=='0':
                all_students = Student.objects.all()
            else:
                all_students = Student.objects.filter(standard=selected_class)

        #  For the message sent section
        elif form_type2 == "form2":

    
            message_title = request.POST.get("title")
            message = request.POST.get("message")

            print(message_title,"-----",message)




    return render(request,"staffs/staff_home.html", {"all_students":all_students})

@login_required(login_url='staff-login')
def message_students(request):
    class1=selected_class

    if request.method == 'POST':
       
        message_title = request.POST.get("title")
        message = request.POST.get("message")

        print(message_title,message, class1)

        m=std_messages()
        m.std_standard = class1
        m.head = message_title
        m.content = message

        m.save()
        

    # return HttpResponse("message ent sucsc")

    return redirect("staff-loginpage")



def staff_login(request):   

    if request.method == 'POST':

        uname= request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request,username=uname,password =pass1)

       

        if user is not None:
            login(request,user)
            return redirect("staff-loginpage")
        
        else:
            return HttpResponse("username or password is wrong!")

    return render(request,"staffs/staffs_login.html")




def staff_signup(request):
    if request.method =='POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1!=pass2:
            return HttpResponse("your password doesn't match")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect("staff-login")
        

    return render(request,"staffs/staffs_signup.html")   



def logout_section(request):
    logout(request)
    return redirect("staff-login")



# """ FOR STUDENT ADD SECITIONS """
@login_required(login_url='staff-login')
def add_student(request):
    if request.method == "POST":
        print("student added")
        roll_mumber = request.POST.get("roll")
        name = request.POST.get("name")
        std = request.POST.get("std")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass1")

        print(roll_mumber,name,std,mobile,email,uname,pass1)

        s=Student()
        s.roll_number = roll_mumber
        s.name = name
        s.standard = std
        s.mobile =  mobile
        s.email = email
        s.username = uname
        s.password = pass1

        s.save()




    return render(request,"staffs/add_student.html")

@login_required(login_url='staff-login')
def delete_student(request,roll_number):

    print(roll_number)
    s= Student.objects.get(roll_number=roll_number)
    s.delete()
    return redirect('staff-loginpage')



@login_required(login_url='staff-login')
def update_student(request,roll_number):

    s= Student.objects.get(roll_number=roll_number)
    print(s.name)
    print(s.mobile)
    if request.method == "POST":
        print("student added")
        roll_mumber = request.POST.get("roll")
        name = request.POST.get("name")
        std = request.POST.get("std")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass1")

        print(roll_mumber,name,std,mobile,email,uname,pass1)

        s=Student()
        s.roll_number = roll_mumber
        s.name = name
        s.standard = std
        s.mobile =  mobile
        s.email = email
        s.username = uname
        s.password = pass1

        s.save()
        return redirect("staff-loginpage")

    return render(request,"staffs/update_student.html",{"std_details":s})


@login_required(login_url='staff-login')
def student_details(request,roll_number,name):
    # return HttpResponse(f"Hello Student {roll_number} {name}" )

    return render(request,"staffs/student_details.html",{"roll_number":roll_number,"name":name} )



    
  