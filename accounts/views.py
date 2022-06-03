from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from projomania_pages.form import SignUpForm
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    
    if request.method =="POST":
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # user = authenticate(request,username=username,password=password)
        # if user is None:
        #     context = {"error":"invalid username or password"}
        #     return render(request,"accounts/login.html", context)
        # login(request, user)
        # return redirect('/')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            print(login(request, form.get_user()))
            print(form.get_user().id)
            if login(request, form.get_user()) == None:
                if form.get_user().id == 1:
                     return redirect(f'/admin')
                return redirect(f'/profile/{form.get_user()}')
        else:
            invalid = "invalid login"
            context = {"invalid":invalid}
            return render(request,"accounts/login.html", context)
    else:
        form = AuthenticationForm(request)
    context = {"form":form}
    return render(request,"accounts/login.html", context)
@login_required
def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect("/")
    return render(request,"accounts/logout.html", {})

def register_view(request):
    form = SignUpForm(request.POST or None)
    
    if form.is_valid() :
        user_obj = form.save()
        return redirect('/login')
    elif form.is_valid() and not form.clean_password2():
        msg = "Please Check the Password"
        context = {"msg":msg}
        return render(request,"accounts/register.html", context)
    # elif form.clean_password2() != False:
    #     msg = "error"
    # elif :
    #     msg = "error"

    context = {"form":form }
    return render(request,"accounts/register.html", context)

@login_required
def user_profile(request,id):
    user = get_object_or_404(User,id=id)
    return render(request,"accounts/profile.html",{"user":user})

def profile(request,slug):
    profileUrl = get_object_or_404(User,id=id)
    context = {"profileUrl":profileUrl}
    return render(request,"accounts/profile.html",context)