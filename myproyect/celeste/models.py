from django.db import models

class usuario(models.model):
	nombre = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=50)
	telefono = models.CharField(max_length=13)
	ciudad = models.CharField(max_length=30)
	pais = models.CharFiel(max_length=30)
	
class correo(models.model):
	email = models.EmailField()
	
	
class comentario(models.model):
	nombre = models.CharField(max_length=30)
	email = models.EmailField()
	telefono = models.CharField(max_length=13)
	

class productos(models.model):
	producto = models.CharField(max_length=30)
	talla = models.CharField(max_length=3)
	color = models.CharField(max_length=30)
	precio = models.CharField(max_length=30)
	categoria = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=30)
	estado = models.CharField(max_length=30)
	

class categorias(models.model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=30)
	estado = models.CharField(max_length=20)
	

class detalleregistro(models.model):
	cantidad = models.CharField(max_length=10)
	
	
class registroproducto(models.model):
	 fecha_registro= models.DateField(max_length=30)
	


