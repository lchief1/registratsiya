from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.lastname}"
