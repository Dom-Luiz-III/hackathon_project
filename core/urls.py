from django.urls import path

from .views import index, login, home


urlpatterns = [
    path('', index, name='admin'),
    path('home', index, name='home'),
    path('login', login, name='login'),
    path('homealuno', home, name='homealuno'),
]
