from django.urls import path
from .views import recognize_user
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('recognize', recognize_user),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)