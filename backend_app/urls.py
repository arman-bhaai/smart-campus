from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'backend_app_home'),
]