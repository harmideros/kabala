from django.db import models

# Create your models here.
class Registrar(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	fecha_nacimiento = models.CharField(max_length=20)
	doc = (
		('NIT', 'NIT'),
		('CC', 'CC'),
		('CE', 'CE'),
		('TI', 'TI'),
		)
	tipo_documento = models.CharField(max_length=3, choices = doc)
	numero_documento = models.CharField(max_length=10)
	email = models.EmailField()
	usuario = models.CharField(max_length=50)
	contraseña = models.CharField(max_length=50)

	def __str__(self):
		return self.usuario

class Comentario(models.Model):
	nombre_apellido = models.CharField(max_length=40)
	email = models.EmailField()
	celular = models.IntegerField()
	mensaje = models.TextField()