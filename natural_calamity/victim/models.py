from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class adminDB(models.Model):  # model for patient
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Volunteer(models.Model):  # model for patient
    Volunteer_name = models.CharField(max_length=200)
    Volunteer_address = models.CharField(max_length=200)
    Volunteer_number = models.CharField(max_length=10)
    Volunteer_email = models.CharField(max_length=200)
    Volunteer_pass = models.CharField(max_length=200)
    Volunteer_maxcapacity = models.IntegerField(default=0)

    def __str__(self):
        return self.Volunteer_name


# Create your models here.
