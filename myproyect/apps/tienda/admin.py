from django.contrib import admin
from .models import Producto

# Register your models here.
class AdminProducto(admin.ModelAdmin):
	list_display = ["__str__", "categoria", "descripcion", "foto", "talla"]
	class Meta:
		model = Producto

admin.site.register(Producto, AdminProducto)