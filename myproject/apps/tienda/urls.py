from django.conf.urls import include, url
from .views import AgregarProducto

urlpatterns = [
	url(r'^', AgregarProducto.as_view(), name="agregar"),
]
