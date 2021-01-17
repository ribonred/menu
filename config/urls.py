from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SpaPage

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",include('appmanager.menu.urls')),
    path("",SpaPage.as_view(),name='spa'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)