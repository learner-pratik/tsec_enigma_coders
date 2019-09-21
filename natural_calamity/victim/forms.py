from django import forms
from .models import adminDB, Volunteer,Login



class Volunteerform(forms.ModelForm):
    class Meta:
        model = Volunteer
        exclude = ()


class Adminform(forms.ModelForm):
    class Meta:
        model = adminDB
        exclude = ()

class Loginform(forms.ModelForm):
    class Meta:
        model = Login
        fields = ["username", "password"]
