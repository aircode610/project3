from django.contrib import admin

from .models import User, Pizza, Topping, Sub, Pasta, Salad, Dinner_Platter, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_Platter)
admin.site.register(Order)
