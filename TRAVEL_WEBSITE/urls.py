












from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('', include('travello.urls')),
    #path('', include('calc.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)