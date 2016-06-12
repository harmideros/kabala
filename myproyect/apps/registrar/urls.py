from django.conf.urls import include, url
from .views import Registro, Comentar

urlpatterns = [
	url(r'^registrar/', Registro, name="registro"),
	url(r'^', Comentar, name="comentar",),
]
