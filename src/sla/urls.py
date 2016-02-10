from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import regbackend


urlpatterns = [
    # Examples:
    url(r'^$', 'introapp.views.home', name='home'),
    url(r'^about/$', 'sla.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', regbackend.MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)