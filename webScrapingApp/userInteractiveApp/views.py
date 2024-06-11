from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AmazonLinkForm
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'you registered successfully')
            return redirect('index')
    else:
        form = SignUpForm
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have been logged in')
            return render(request, 'login.html')
        else:
            messages.error(request, 'login failed')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out')
    return redirect('index')


def scrape_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AmazonLinkForm(request.POST)
            if form.is_valid():
                scraped_data = form.save(commit=False)
                scraped_data.user = request.user
                scraped_data.save()
                return redirect('scrape_success')  # Redirect to a success page
        else:
            form = AmazonLinkForm()
            return render(request, 'amazonwebscraper.html', {'form': form})
        return render(request, 'amazonwebscraper.html', {'form': form})
    messages.success(request, 'you have to be logged in to scrape data')
    return render(request, 'amazonwebscraper.html')
