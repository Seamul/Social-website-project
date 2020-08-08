from django import forms
from .model import Profile2

class  Profile2EditForm(forms.ModelForms):
	class Meta:
		fields=1
			