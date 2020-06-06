from django.contrib import admin


from .models import User, Food, Topping, Order, Food_topping

# Register your models here.
admin.site.register(User)
admin.site.register(Food)
admin.site.register(Topping)
admin.site.register(Food_topping)
admin.site.register(Order)
