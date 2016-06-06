from django.shortcuts import render

# Create your views here.
#from .forms import LoginForm
from django.contrib import auth
from .forms import LoginForm
from .models import Login

def LoginIni(request):
#	form = LoginForm(request.POST or None)
#	context = {
#		"form":form
#	}

#	if form.is_valid():
#		form_data = form.cleaned_data
#		usr = form_data.get("usuario_form")
#		cont = form_data.get("contraseña_form")
#		obj = Login.objects.create(usuario=usr, contraseña=cont)
	username = request.POST.get('usuario','')
	password = request.POST.get('contraseña','')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect

	titulo = "Iniciar sesion"
	nom = ""
	form = LoginForm(request.POST or None)

	context = {
		"titulo": titulo,
		"form": form,
		"nom": nom
	}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("usuario")
		form.save()

		context = {
			"nom": "%s - " %(nombre),
			"titulo": "cerrar sesion"
		}
#		print(instance)
#	if request.user.is_authenticated():
#		titulo = "Hola, %s!" %(request.user)


	return render(request, "index.html", context)