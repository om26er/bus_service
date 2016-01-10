from django.contrib.auth.models import AbstractUser
from django.db import models


class DriverModel(AbstractUser):

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    bus_number = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'username'


# class StudentModel(AbstractUser):
#
#     fee_paid = models.BooleanField()
#     route_name = models.CharField(max_length=200)