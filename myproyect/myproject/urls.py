from django.conf.urls import include, url
from django.contrib import admin
from myproject.views import celeste, moda, sobre, tienda, contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', celeste, name="home"),
    url(r'^moda/$', moda),
    url(r'^sobre/$', sobre, name="about"),
#    url(r'^tienda/$', tienda),
#    url(r'^contacto/$', contacto),
    url(r'^tienda/', include('apps.tienda.urls'), name="tienda"),
#    url(r'^home/', include('apps.login.urls')),
    url(r'^registro/', include('apps.registrar.urls')),
    url(r'^contacto/', include('apps.registrar.urls')),
    url(regex=r'^media/(?P<path>.*)$',
			view='django.views.static.serve',
			kwargs={'document_root': settings.MEDIA_ROOT}),
#    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, } ),
    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

#if settings.DEBUG:
#	urlpatterns.append(
#		url(regex=r'^media/(?P<path>.*)$',
#			view='django.views.static.serve',
#			kwargs={'document_root': settings.MEDIA_ROOT}))