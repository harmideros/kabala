from django.contrib import admin

# Register your models here.
from .forms import RegistrarForm, ComentarioForm
from .models import Registrar, Comentario

# Register your models here.
class AdminRegistrar(admin.ModelAdmin):
	list_display = ["__str__", "email"]
#	fields = ("nombre", "apellidos")
	form = RegistrarForm
#	class Meta:
#		model = Login
admin.site.register(Registrar, AdminRegistrar,)

class AdminComentario(admin.ModelAdmin):
	list_display = ["email"]
	form = ComentarioForm


admin.site.register(Comentario, AdminComentario)
