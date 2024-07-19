from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

#URLS APP

urlpatterns = [
    path('', views.home),
    path('acerca', views.about),
    path('bienvenido', views.welcome),
    path('contacto', views.contact),
    path('exito', views.exito),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup)
]