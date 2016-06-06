from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		fields = ["usuario", "contraseña"]

	def __init__(self, *args, **kwars):
		super().__init__(*args, **kwars)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

		self.fields['usuario'].widget.attrs.update({'placeholder': 'usuario'})
		self.fields['contraseña'].widget.attrs.update({'placeholder': 'contraseña'})

	#def clean_usuario(self):
		#nom = self.cleaned_data.get("usuario")
		#if not "edu" in nom:
		#	raise forms.ValidationError("Por favor digite un usuario correcto")
		#return nom 

#class RegLog(forms.Form):
#	usuario_form = forms.CharField(max_length=100)
#	contraseña_form = forms.CharField() 