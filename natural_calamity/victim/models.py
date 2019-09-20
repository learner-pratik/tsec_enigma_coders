from django.db import models


class Victim(models.Model):  # model for patient
    Victim_name = models.CharField(max_length=200)
    Victim_address = models.CharField(max_length=200)
    Victim_number = models.CharField(max_length=10)
    Victim_email = models.CharField(max_length=200)
    Victim_pass = models.CharField(max_length=200)

    def __str__(self):
        return self.Victim_name


class Volunteer(models.Model):  # model for patient
    Volunteer_name = models.CharField(max_length=200)
    Volunteer_address = models.CharField(max_length=200)
    Volunteer_number = models.CharField(max_length=10)
    Volunteer_email = models.CharField(max_length=200)
    Volunteer_pass = models.CharField(max_length=200)
    Volunteer_designation=models.CharField(max_length=200)
    Volunteer_maxcapacity=models.IntegerField(default=0)

    def __str__(self):
        return self.Volunteer_name

# Create your models here.
