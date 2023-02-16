from django.urls import path
from . import views

urlpatterns = [
    path('access/', views.access_mail)
]