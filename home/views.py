from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from .models import Contact
from blog.models import Blogpost
# Create your views here.
# hame page and basic functionality view
def homepage(request):
    post = Blogpost.objects.all().order_by('-time_stamp')
    return render(request,'hometemps/home.html',{'post':post})

# managing contact us page
def contactus(request):
    # messages.error(request,'Welcome to contact')
    if request.method == "POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        
        if len(name)<2 or len(email)<10 or len(phone)<7 or len(desc)<20:
            messages.error(request,'Please fill the form correctly!')
        else:
            contact = Contact(user_name =name, user_email =email,user_phone = phone, message_content = desc)
            contact.save()
            messages.success(request,'Your message has been sent.')
            thank = True
            return render(request,'hometemps/contactus.html',{'thank':thank})
    return render(request,'hometemps/contactus.html')

# handling about us
def aboutus(request):
    return render(request,'hometemps/aboutus.html')

# search query functionality
def searchbox(request):
    search_query = request.GET['searchbox']
    if len(search_query)>50:
        found_data = Blogpost.objects.none()
    else:
        found_datatitle = Blogpost.objects.filter(title__icontains = search_query)
        found_datacontent = Blogpost.objects.filter(blog_content__icontains = search_query)
        found_dataauther = Blogpost.objects.filter(auther__icontains = search_query)
        found_data = found_datatitle.union(found_datacontent,found_dataauther)
    if found_data.count() == 0:
        messages.error(request,'Please Enter the correct search query!')
    search_content = {'found_data':found_data,'query':search_query}
    return render(request,'hometemps/search.html',search_content)
    
# handling signup function
def handlesignup(request):
    if request.method == 'POST':
        # Getting POST parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        #  Checks for error input
        # user name length check
        if len(username)>10:
            messages.error(request,'User name is too lengthy, must be under 10 characters')
            return redirect('Home')
        # user name alphanumeric check
        if not username.isalnum():
            messages.error(request,'Username must be alphanumberic. Username should not contain any special character')
            return redirect('Home')
        # password check
        if password != confirmpassword:
            messages.error(request,'Password does not match')
            return redirect('Home')

        # Creating the user
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        try:
            myuser.save()
            messages.success(request,'Your account has been successfully registed')
            return redirect('Home')
        except:
            messages.error(request,'user already exists')
            return redirect('Home')
    else:
        return HttpResponse('404 - Not Found')

# handling login function
def handlelogin(request):
    if request.method == 'POST':
        # Getting POST parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in successfully')
            return redirect('Home')
        else:
            messages.error(request,'Invalid credentials,Please try again')
            return redirect('Home')
            
    return HttpResponse('404 - Not Found')
def handlelogout(request):
   
    logout(request)
    messages.success(request,'Successfully Logged out')
    return redirect('Home')

