from django import forms
from .models import adminDB, Volunteer


class Volunteerform(forms.ModelForm):
	class Meta:
		model = Volunteer
		exclude = ()

class Adminform(forms.ModelForm):
	class Meta:
		model = adminDB
		exclude = ()