from django import forms

from .models import Victim


class Victimform(forms.ModelForm):
	class Meta:
		model = Victim
		exclude = ()