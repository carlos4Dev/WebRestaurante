"""webrestaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menu import views
from menu.urls import menu_patterns
from profiles.urls import profiles_patterns
from django.conf import settings

from rest_framework import routers

router = routers.DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('pedidos', views.PedidosViewSet)

urlpatterns = [
    # Path del core
    path('', include('core.urls')),
    # Path del menu
    path('menu/', include(menu_patterns)),
    path('menu/', include('menu.urls')),
    # Path del admin
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),

    # Paths de la API
    path('menu/v1/', include(router.urls)),
    path('menu/v1/terminado/', views.CambiarEstadoPedido.as_view())
]
