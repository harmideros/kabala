from django import forms
from .models import Registrar, Comentario

class RegistrarForm(forms.ModelForm):
	class Meta:
		model = Registrar
		fields = ["nombre", "apellidos", "fecha_nacimiento", "tipo_documento", "numero_documento", "email", "usuario", "contraseña"]

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ["nombre_apellido", "email", "celular", "mensaje"]
	def __init__(self, *args, **kwars):
		super().__init__(*args, **kwars)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

		self.fields['nombre_apellido'].widget.attrs.update({'placeholder': 'Nombre y apellido'})
		self.fields['email'].widget.attrs.update({'placeholder': 'Email@example.com'})
		self.fields['celular'].widget.attrs.update({'placeholder': 'Numero de celular 000-000-0000'})
		self.fields['mensaje'].widget.attrs.update({'placeholder': 'Cuerpo del mensaje'})
