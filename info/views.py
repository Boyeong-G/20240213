from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from info.forms import LoginForm, UserForm

@login_required(login_url='login')
def info_my(request):
    
    return render(
        request,
        'info/info_my.html'
    )

def login_signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST["next"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next)
        else:
            form = LoginForm()
            return render(
                request,
                'info/login.html',
                {
                    'form': form,
                    'error':'Username or Password is incorrect.',
                }
            )
    else:
        next = request.GET["next"]
        form = LoginForm()
        return render(
            request,
            'info/login.html',
            {
                'form': form,
                'next': next,
            }
        )
    
    return render(
        request,
        'info/login.html',
        {
            'form': form
        }
    )

def signup_signin(request):
    if request.method == "POST":
        next = request.POST["next"]
        
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        if not (first_name or email):
            form = UserForm(request.POST)
            return render(
                request,
                'info/signup.html',
                {
                    'form': form,
                    'next':next,
                    'error': 'Please enter your name or email.'
                }
            )
        elif User.objects.filter(username=username).exists():
            form = UserForm(request.POST)
            return render(
                request,
                'info/signup.html',
                {
                    'form': form,
                    'next':next,
                    'error': 'The ID that already exists.'
                }
            )
        elif User.objects.filter(email=email).exists():
            form = UserForm(request.POST)
            return render(
                request,
                'info/signup.html',
                {
                    'form': form,
                    'next':next,
                    'error': 'This email is already registered.'
                }
            )
        
        form = UserForm(request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                first_name = form.cleaned_data["first_name"]
                password = form.cleaned_data["password"]
                user_create = User.objects.create_user(username, email, password, first_name=first_name)
                user_create.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect(next)
        except:
            return render(
                request,
                'info/signup.html',
                {
                    'form': form,
                    'next':next,
                    'error': 'Either the member exists or the password format is too simple.'
                }
            )
            
    else:
        next = request.GET["next"]
        form = UserForm()
        return render(
            request,
            'info/signup.html',
            {
                'form': form,
                 'next':next,
            }
        )
        
    return render(
        request,
        'info/signup.html',
        {
            'form': form
        }
    )
    
def logout_sign(request):
    next = request.GET["next"]
    logout(request)
    
    return redirect(next)