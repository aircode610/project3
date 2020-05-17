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
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    )
    KIND = (
        ('C', 'Cheese'),
        ('1', '1 topping'),
        ('2', '2 toppings'),
        ('3', '3 toppings'),
        ('S', 'Special'),
    )
    SIZE = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=1, choices=NAME)
    kind = models.CharField(max_length=1, choices=KIND)
    size = models.CharField(max_length=1, choices=SIZE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.kind} ( {self.size} ) : {self.price}"


class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Sub(models.Model):
    SIZE = (
        ('S', 'Small'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=20)
    size = models.CharField(max_length=1, choices=SIZE)
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
        ('S', 'Small'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=20)
    size = models.CharField(max_length=1, choices=SIZE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.size}) : {self.price}"
