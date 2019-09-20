from django import forms
from .models import adminDB, Volunteer

class Victimform(forms.ModelForm):
	class Meta:
		model = adminDB
		exclude = ()

class Volunteerform(forms.ModelForm):
	class Meta:
		model = Volunteer
		exclude = ()