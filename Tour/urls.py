"""Tour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from task import views as tv
from task.models import Turista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tv.hello, name="Home"),
    path('', tv.Exilio, name="Exilio"),
    path('login/', tv.login_us, name="login"),
    path('registr/', tv.R_agente, name="registr"),
    path('logout/', tv.X_sesion, name="logout"),
    path('cuenta/', tv.ver_cuenta, name="cuenta"),
    path('Encuesta/P1', tv.R_Turista, name="EnTurista"),
    path('Encuesta/P2/<cedu>', tv.Create_Cuestionario, name="EnQuest"),
]
