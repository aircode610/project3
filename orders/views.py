from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.core.mail import send_mail

from .models import User, Food, Topping, Order, Food_topping

import random
import json

# Create your views here.
def index(request):

    try:

        if request.session["logged_in"] == False:
            return HttpResponseRedirect(reverse("signin"))
        else:

            object = Food.objects.all()

            foods = []
            for food in object:
                foods.append({
                    "type" : food.type,
                    "name" : food.name,
                    "can_have_topping" : food.can_have_topping,
                    "exact_number_of_toppings" : food.exact_number_of_toppings,
                    "small_price" : food.small_price,
                    "large_price" : food.large_price,
                    "each_topping_price" : food.each_topping_price
                })

            food_toppings = []
            for food_topping in Food_topping.objects.all():

                toppings = []
                for topping in food_topping.toppings.all():
                    toppings.append(topping.name)

                food = ""
                for food in food_topping.food.all():
                    food = food.name

                food_toppings.append({
                    "food" : food,
                    "toppings" : toppings
                })

            context = {
                "username" : request.session["username"],
                "food" : json.dumps(foods),
                "toppings" : json.dumps(food_toppings)
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
    request.session["username"] = info["username"]

    return HttpResponseRedirect(reverse("index"))


def login(request):
    context = {
        "users" : User.objects.all()
    }

    return render(request, "orders/login.html", context)


def login_user(request):
    request.session["logged_in"] = True
    username = request.POST["username"]

    users =  User.objects.all()

    for user in users:
        if user.username == request.POST["username"]:

            request.session["user_info"] = { "name" : user.name, "lastname" : user.lastname,
             "email" : user.email, "username" : username, "password" : user.password }

            request.session["username"] = user.username

            break

    return HttpResponseRedirect(reverse("index"))


def logout(request):
    request.session["logged_in"] = False

    return HttpResponseRedirect(reverse("index"))


def order(request):
    cart = json.loads(request.POST.get('cart'))
    price = json.loads(request.POST.get('price'))

    new_order = Order(orders=cart, price=price)
    new_order.save()

    send_mail(
        'Thanks for ordering pizza from our website!',
        'Don\'t forget, always eat pizza! ;) ',
        'aircode610@gmail.com',
        [request.session["user_info"]["email"]],
        fail_silently=False
    )

    return HttpResponseRedirect(reverse("index"))
