# from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, ListView
from .models import Producto


class AgregarProducto(ListView):
	template_name = 'tienda/index.html'
	model = Producto
	context_object_name = 'productos'