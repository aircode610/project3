from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.core.mail import send_mail

from .models import User, Pizza, Topping, Sub, Pasta, Salad, Dinner_Platter

import random

# Create your views here.
def index(request):
    try:
        if request.session["logged_in"] == False:
            return HttpResponseRedirect(reverse("signin"))
        else:
            context = {
                "username" : request.session["username"]
            }
            return render(request, "orders/index.html", context)
    except:
        request.session["logged_in"] = False
        return HttpResponseRedirect(reverse("signin"))


def signin(request):
    context = {
        "users" : User.objects.all()
    }

    return render(request, "orders/signin.html", context)

def verify(request):
    email = request.POST["email"]
    code = random.randint(1000, 9999)
    content = f"Your code: {code}"

    name = request.POST["name"]
    lastname = request.POST["lastname"]
    username = request.POST["username"]
    password = request.POST["password"]

    request.session["user_info"] = { "name" : name, "lastname" : lastname, "email" : email,
                                    "username" : username, "password" : password }

    send_mail(
        'Email verification',
        content,
        'aircode610@gmail.com',
        [email],
        fail_silently=False
    )

    context = {
        "code" : code
    }

    return render(request, "orders/verify.html", context)


def add_user(request):
    info = request.session["user_info"]

    new_user = User(name=info["name"], lastname=info["lastname"], email=info["email"],
                    username=info["username"], password=info["password"])
    new_user.save()

    request.session["logged_in"] = True

    return HttpResponseRedirect(reverse("index"))


def login(request):
    context = {
        "users" : User.objects.all()
    }

    return render(request, "orders/login.html", context)


def login_user(request):
    request.session["logged_in"] = True

    return HttpResponseRedirect(reverse("index"))


def logout(request):
    request.session["logged_in"] = False

    return HttpResponseRedirect(reverse("index"))
