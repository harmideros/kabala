from django.contrib import admin

# Register your models here.
from .forms import LoginForm
from .models import Login

# Register your models here.
class AdminLogin(admin.ModelAdmin):
	list_display = ["__str__"]
	form = LoginForm
#	class Meta:
#		model = Login

admin.site.register(Login, AdminLogin)