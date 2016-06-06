from django.conf.urls import include, url
from .views import LoginIni

urlpatterns = [
	url(r'^', LoginIni, name="login"),
]
