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


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Food(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    can_have_topping = models.IntegerField()
    exact_number_of_toppings = models.IntegerField()
    small_price = models.FloatField()
    large_price = models.FloatField()
    each_topping_price = models.FloatField()


    def __str__(self):
        return f"{self.name}"


class Food_topping(models.Model):
    food = models.ManyToManyField(Food, blank=True, related_name="food")
    toppings = models.ManyToManyField(Topping, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.food.name} : {self.toppings.name}"


class Order(models.Model):
    orders = models.CharField(max_length=1000)
    price = models.FloatField()

    def __str__(self):
        return f"{self.orders} : {self.price}"
