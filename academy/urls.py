from django.urls import path
from . import views

urlpatterns = [
    path('', views.academy, name="academy")
]