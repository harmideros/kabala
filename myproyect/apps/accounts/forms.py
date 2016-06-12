from django.utils.translation import ugettext as _

from django import forms
from django.contrib.auth.models import User


class RegistroUserForm(forms.Form):

	username = forms.CharField(label='Usuario', min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Correo Electronico' ,widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Contraseña', min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 =forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	photo = forms.ImageField(label='Foto', required=False)

	def clean_username(self):

		username= self.cleaned_data['username']
		if User.objects.filter(username=username):
			raise forms.ValidationError('Nombre de usuario ya registrado.')
		return username

	def clean_email(self):

		email= self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('Ya existe un email igual en la db.')
		return email

	def clean_password2(self):

		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError(_('Las contraseñas no coinciden.'))
		return password2

class EditarEmailForm(forms.Form):

	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request')
		return super().__init__(*args, **kwargs)

	def clean_email(self):
		email = self.cleaned_data['email']
		actual_email = self.request.user.email
		username = self.request.user.username
		if email != actual_email:
			existe = User.objects.filter(email=email).exclude(username=username)
			if existe:
				raise forms.ValidationError('Ya existe un email igual en la db')
		return email

class EditarContrasenaForm(forms.Form):

	actual_password = forms.CharField(label='Contraseña actual', min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	
	password = forms.CharField(label='Nueva contraseña', min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	
	password2 = forms.CharField(label='Repetir contraseña', min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	def clean_password2(self):
		password =self.cleaned_data['password']
		password2 =self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError('Las contraseñas no coinciden.')
		return password2