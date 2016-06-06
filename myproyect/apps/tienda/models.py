from django.db import models

# Create your models here.
class Producto(models.Model):
	ref = models.AutoField(primary_key=True)
	categoria = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=30, blank=True, null=True)
	TALLA = (
		('XS', 'XS'),
		('S', 'S'),
		('M', 'M'),
		('L', 'L'),
		('XL', 'XL'),
		)
	talla = models.CharField(max_length=2, choices = TALLA)
	precio = models.FloatField()
#	publicacion = models.DateTimeField(auto_now=True, auto_now_add=False)
	foto = models.ImageField(upload_to='productos')

	def __str__(self):
		return ' - ref: ' + str(self.ref)
