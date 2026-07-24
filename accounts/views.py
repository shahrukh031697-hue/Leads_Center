from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests


def login_user(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(request, 'login.html')


@login_required(login_url='login')
def home_page(request):

    return render(request, 'home.html')


def logout_user(request):

    logout(request)

    return redirect('login')


def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        program = request.POST.get('program')
        message = request.POST.get('message')

        data = {
            "name": name,
            "phone": phone,
            "email": email,
            "program": program,
            "message": message
        }

        google_sheet_url = "https://script.google.com/macros/s/AKfycbywZFsE3QPEzo178ZioWdRnY9HSppMNoOIgiA_qlVpnieYf8P_-eJdO-dYSgcSaCBQ/execgit"

        requests.post(
            google_sheet_url,
            json=data
        )

        return redirect('home')

    return redirect('home')