from django import forms
from .models import Bailarines
from .models import Instructor_danza
from django.contrib.auth.forms import UserCreationForm

class Bailarines_form(forms.ModelForm):
	class Meta:
		model = Bailarines
		fields = '__all__'
class Instructores_form(forms.ModelForm):
	class Meta:
		model = Instructor_danza
		fields = '__all__'

class Trainer_form(UserCreationForm):
	mail = forms.CharField(max_length=50)
	phone = forms.IntegerField()

class Consulta_form(forms.ModelForm):
	class Meta:
		model = Instructor_danza
		fields = '__all__'

class Ingresar(forms.Form):
	id_detail = forms.IntegerField()