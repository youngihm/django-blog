from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from .forms import LoginForm,RegisterForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("list")
            return render(request, "account.html",{"form":form})



    else:
        form = LoginForm()
        return render(request, "account.html",{"form":form})


def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        #폼으로 받은 데이터로 유저 만들어야해서
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            #회원가입하자마자로그인된상태
            login(request,user)
            return redirect("list")

    else:
        form = RegisterForm()
        return render(request, "account.html",{"form":form})
