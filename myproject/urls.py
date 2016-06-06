from django.conf.urls import include, url
from django.contrib import admin
from myproject.views import celeste, moda, sobre, tienda, contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^home/$', celeste),
    url(r'^moda/$', moda),
    url(r'^sobre/$', sobre),
#    url(r'^tienda/$', tienda),
#    url(r'^contacto/$', contacto),
    url(r'^tienda/', include('apps.tienda.urls'), name="tienda"),
    url(r'^home', include('apps.login.urls')),
    url(r'^registro/', include('apps.registrar.urls')),
    url(r'^contacto/', include('apps.registrar.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, } ),
    url(r'^accounts/', include('apps.accounts.urls')),
]

#if settings.DEBUG:
#	urlpatterns.append(
#		url(regex=r'^media/(?P<path>.*)$',
#			view='django.views.static.serve',
#			kwargs={'document_root': settings.MEDIA_ROOT}))