from django.contrib import admin
from django.urls import path
from messirve.views import home,galeria,contacto,save_contact_info
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('galeria/',galeria),
    path('contacto/',contacto),
    path('save_contact_info',save_contact_info),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)