from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.core.mail import send_mail

from .models import User, Pizza, Topping, Sub, Pasta, Salad, Dinner_Platter, Order

import random
import json

# Create your views here.
def index(request):
    try:
        if request.session["logged_in"] == False:
            return HttpResponseRedirect(reverse("signin"))
        else:

            pizzas = []
            for pizza in Pizza.objects.all():
                pizzas.append({
                    "name" : pizza.name,
                    "kind" : pizza.kind,
                    "size" : pizza.size,
                    "price" : pizza.price
                })

            toppings = []
            for topping in Topping.objects.all():
                toppings.append({
                    "name" : topping.name,
                })

            subs = []
            for sub in Sub.objects.all():
                subs.append({
                    "name" : sub.name,
                    "size" : sub.size,
                    "price" : sub.price
                })

            pastas = []
            for pasta in Pasta.objects.all():
                pastas.append({
                    "name" : pasta.name,
                    "price" : pasta.price
                })

            salads = []
            for salad in Salad.objects.all():
                salads.append({
                    "name" : salad.name,
                    "price" : salad.price
                })

            dinners = []
            for dinner in Dinner_Platter.objects.all():
                dinners.append({
                    "name" : dinner.name,
                    "size" : dinner.size,
                    "price" : dinner.price
                })

            food = { "Pizza" : pizzas, "Topping" : toppings, "Sub" : subs,
             "Pasta" :pastas, "Salad" : salads, "Dinner platter" : dinners }

            context = {
                "username" : request.session["username"],
                "food" : json.dumps(food)
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

    users =  User.objects.all()

    for user in users:
        if user.username == request.POST["username"]:

            request.session["user_info"] = { "name" : user.name, "lastname" : user.lastname,
             "email" : user.email, "username" : user.username, "password" : user.password }

            request.session["username"] = user.username

            break

    return HttpResponseRedirect(reverse("index"))


def logout(request):
    request.session["logged_in"] = False

    return HttpResponseRedirect(reverse("index"))


def order(request):
    cart = json.loads(request.POST.get('cart'))
    price = request.POST.get('price')

    orders_str = ""

    for item in cart:
        first_part = str(item).split(":")[0]

        if "-" in first_part:
            if item[0] == "P":
                orders_str += first_part + "("
            if item[0] == "T":
                orders_str += first_part.split(" - ")[1]
                if cart[cart.index(item) + 1][0] == "T":
                    orders_str += ", "
                elif cart[cart.index(item) + 1][0] == "S":
                    orders_str += " ) + "
                else:
                    orders_str += " ), "
            if item[0] == "S":
                orders_str += first_part.split(" - ")[1]
                if cart[cart.index(item) + 1][0] == "S":
                    orders_str += ", "
                else:
                    orders_str += " ), "
        else:
          orders_str += first_part

    new_order = Order(orders=orders_str, price=price)
    new_order.save()

    send_mail(
        'Thanks for ordering pizza from our website!',
        'Don\'t forget, always eat pizza! ;) ',
        'aircode610@gmail.com',
        [request.session["user_info"]["email"]],
        fail_silently=False
    )

    return HttpResponseRedirect(reverse("index"))
