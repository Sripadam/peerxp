from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate 
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import UpdateView, CreateView,DeleteView
from .models import *

# Login into blog
def Login(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, "Invalid credentials.")
            return render(request,'home.html')
        return render(request,"login.html")
    except Exception as e:
        return render(request,"login.html",{"something went wrong"})
# Register post
def register(request):
    try:
        if request.method =="POST":
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['possword2']

            if password1 != password2:
                messages.error(request, "passwords do not match.")
                return redirect('/register')
            user = User.objects.create_user(username, phone,email,password1)
            user.first_name = first_name
            user.last_name = last_name 
            user.save()
            return render(request, 'login.html')
        return render(request,"register.html")
    except Exception as e:
        return render(request,"register.html",{'something missing'})

 # logout blog 
def Logout(request):
    try:
        logout(request)
        messages.success(request,"succefully logged out")
        return redirect('/login')
    except Exception as e:
        return render(request,'home.html',{"something missing"})    

def home(request):

    try:
        posts = Ticket.objects.all()
        posts = Ticket.objects.filter().order_by('-dateTime')
        return render(request, "home.html", {'posts':posts})
    except:
        return render(request,"home.html",{'posts':'try again'})    
def createuser(request):
    try:
        if request.method =="POST":
            username = request.POST['username']
            phone = request.POST['phone']
            email = request.POST['email']
            password = request.POST['password']
            Department = request.POST['Department']
            Role = request.POST['Role']

            
            user = User.objects.create_user(username, phone,email,password,Department,Role)            
            user.save()
            
            return render(request, 'home.html')
        return render(request,"createuser.html")
    except Exception as e:
        return render(request,"createuser.html",{'something missing'})

class AddPostView(CreateView):
    try:

        model = Department
        #form_class = BlogPostForm
        template_name = 'dep_add.html'
        fields = '__all__'
        context_object_name = 'object'
    except Exception as e:
        JsonResponse({'msg':'something missing'})
# Update blog post
class UpdatePostView(UpdateView):
    try:
        model = Department
        template_name = 'dep_edit.html'
        fields = ['name','description']
    except Exception as e:
        JsonResponse({'msg':'something missing'})
class DeletePostView(DeleteView):
    model = Department
    success_url=('/')
    #Department.objects(fields).delete()



def ticket(request):
    if request.method == "POST":
        subject = request.POST['subject']
        body = request.POST["body"]
        email =request.GET(User.email)
        ticket = Ticket.objects.create_ticket(subject,body,email)
        ticket.save()
        return render(request,'home.html')
    return render(request,'ticket.html')

