from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name} {self.lastname} ({self.email} : {self.username} - {self.password})"


class Pizza(models.Model):
    NAME = (
        ('Regular', 'Regular'),
        ('Sicilian', 'Sicilian'),
    )
    KIND = (
        ('Cheese', 'Cheese'),
        ('1 topping', '1 topping'),
        ('2 toppings', '2 toppings'),
        ('3 toppings', '3 toppings'),
        ('Special', 'Special'),
    )
    SIZE = (
        ('Small', 'Small'),
        ('Large', 'Large'),
    )
    name = models.CharField(max_length=10, choices=NAME)
    kind = models.CharField(max_length=10, choices=KIND)
    size = models.CharField(max_length=10, choices=SIZE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.kind} ( {self.size} ) : {self.price}"


class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Sub(models.Model):
    SIZE = (
        ('Small', 'Small'),
        ('Large', 'Large'),
    )

    name = models.CharField(max_length=20)
    size = models.CharField(max_length=10, choices=SIZE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.size}) : {self.price}"


class Pasta(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} : {self.price}"


class Salad(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} : {self.price}"


class Dinner_Platter(models.Model):
    SIZE = (
        ('Small', 'Small'),
        ('Large', 'Large'),
    )

    name = models.CharField(max_length=20)
    size = models.CharField(max_length=10, choices=SIZE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.size}) : {self.price}"


class Order(models.Model):
    orders = models.CharField(max_length=1000)
    price = models.FloatField()

    def __str__(self):
        return f"{self.orders} : {self.price}"
