from django.urls import path
from .views import recognize_user

urlpatterns = [

    path('recognize', recognize_user),
]
