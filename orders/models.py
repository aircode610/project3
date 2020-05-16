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
