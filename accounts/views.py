from django.shortcuts import render, redirect

import requests


def home_page(request):
    return render(request, 'home.html')


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

        google_sheet_url = "https://script.google.com/macros/s/AKfycbywZFsE3QPEzo178ZioWdRnY9HSppMNoOIgiA_qlVpnieYf8P_-eJdO-dYSgcSaCBQ/exec"

        requests.post(
            google_sheet_url,
            json=data
        )

        return redirect('home')

    return redirect('home')

def principal_message(request):
    return render(request, 'principal_message.html')

def caprogram(request):
    return render(request, 'caprogram.html')

def accaprogram(request):
    return render(request, 'accaprogram.html')