from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CustomLoginForm

def index(request):
    return render(request, 'index.html')
 

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # After registration redirect to main page
            return redirect('main')
        else:
            return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # After login redirect to main page
            return redirect('main')
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def main(request):
    return render(request, 'main.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def newar(request):
    context = {'some_data': 'value'}
    return render(request, 'newar.html', context)


def gurung(request):
    return render(request, 'gurung.html')  # ✅ Correct


def rai(request):
    context = {'some_data': 'value'}
    return render(request, 'rai.html', context)


def chhetri(request):
    return render(request, 'chhetri.html')

def tharu(request):
    return render(request, 'tharu.html')

def sherpa(request):
    return render(request, 'sherpa.html')
