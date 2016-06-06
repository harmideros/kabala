from django.db import models

# Create your models here.

class Login(models.Model):
	usuario = models.CharField(max_length=100)
	contraseña = models.CharField(max_length=50)

	def __str__(self):
		return self.usuario