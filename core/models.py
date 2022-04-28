from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    Options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('trans', 'Prefer not to say')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200, choices=Options)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.user.first_name


class Appointment(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
