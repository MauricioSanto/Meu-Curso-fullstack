from django.urls import path
from . import views

urlpatterns = [
    path('apresentacao/', views.saudacao)
]
