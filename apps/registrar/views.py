from django.shortcuts import render

# Create your views here.

from .forms import RegistrarForm, ComentarioForm
from .models import Registrar, Comentario

def Registro(request):
#	form = LoginForm(request.POST or None)
#	context = {
#		"form":form
#	}

#	if form.is_valid():
#		form_data = form.cleaned_data
#		usr = form_data.get("usuario_form")
#		cont = form_data.get("contraseña_form")
#		obj = Login.objects.create(usuario=usr, contraseña=cont)

	titulo = "Crear Cuenta"
	form = RegistrarForm(request.POST or None)

	context = {
		"titulo": titulo,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("usuario")
		form.save()

		context = {
			"titulo": "Gracias %s, ya esta registrado." %(nombre)
		}
#		print(instance)
#	if request.user.is_authenticated():
#		titulo = "Hola, %s!" %(request.user)


	return render(request, "registro/index.html", context)


def Comentar(request):
#	form = LoginForm(request.POST or None)
#	context = {
#		"form":form
#	}

#	if form.is_valid():
#		form_data = form.cleaned_data
#		usr = form_data.get("usuario_form")
#		cont = form_data.get("contraseña_form")
#		obj = Login.objects.create(usuario=usr, contraseña=cont)

	titulo = "Crear Cuenta"
	form = ComentarioForm(request.POST or None)

	context = {
		"titulo": titulo,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre_apellido")
		form.save()

		context = {
			"titulo": "Gracias %s, por tu comentario." %(nombre)
		}
#		print(instance)
#	if request.user.is_authenticated():
#		titulo = "Hola, %s!" %(request.user)


	return render(request, "contacto.html", context)