from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# usuario personalizado
from cuenta.forms import *
from django.contrib import messages
#
from django.contrib.auth.forms import UserCreationForm
from task.forms import *

#from .models import *
from task.custom import *
#

def Mostrar_estadisticas(request):
    info = Estadisticas_por_ciudad("pereira")
    paquete = {"Turi": info}
    return render(request,"Estadistica.html", paquete )

def hello(request):
    info = Estadisticas_por_ciudad("pereira")
    paquete = {"Turi": info}
    return render(request,"index.html", paquete )

def Exilio(request):
    paquete = {"Exiliado": "Arriba"}
    return render(request,"Exilio.html", paquete )

def login_us(request):
    if request.method == "GET":
            paquete = {'form': AccountAuthenticationForm}
            return render(request,"login.html", paquete )
    else:
        datos = request.POST
        form    = AccountAuthenticationForm(datos)
        email   = datos.get('email')
        password = datos.get('password')
        us =  authenticate(email=email, password=password)
        print(us)
        if us:
            login(request,us)
            messages.success(request, "Logged In")
            return redirect("Home")
        else:
            messages.error(request,"Parece que hay un error :v")
            return redirect("login")
# registrar agente
def R_agente(request):
    if request.method == "GET":
        
        paquete = {'form': RegistrationForm}
        return render(request,"registro_agente.html", paquete )
    else:
        datos = request.POST
        form = RegistrationForm(datos)
        if form.is_valid():
            form.save()# almacenar BD
            email    = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            us = authenticate(email=email, password = raw_pass)
            login(request, us) # guardar sesion
            return redirect('Home')
            
        else:
            paquete = {
                'nombre': request.POST["username"],
                'error': "las contraseñas no coinciden"
            }
            return render(request,"index.html", paquete )
#cerrar sesion
def X_sesion(request):
    logout(request)
    return redirect("Home")

def Create_Cuestionario(request, cedu):
    if request.user.is_authenticated:
        if request.method == "GET":
                paquete = {'form': CreateCuestionario}
                return render(request,"cuestionario2.html", paquete )
        else:
            datos = request.POST
            form = CreateCuestionario(datos)
            NQuest = form.save(commit=False)
            NQuest.user = request.user
            NQuest.cuestionado = Turista.objects.get(cedula = cedu)
            NQuest.agente = request.user
            NQuest.save()# guarda en la base de datos
            print(datos.get("save_exit"))
            if datos.get("save_next"):
                return redirect("EnTurista")
            elif datos.get("save_exit"):
                return redirect("Home")
            else:
                paquete = {'Exiliado': 'cuestionario2' }
                return render(request,"Exilio.html", paquete )
    else:
        paquete = {'Exiliado': 'El exterior' }
        return render(request,"Exilio.html", paquete )

def ver_cuenta(request):
    if not request.user.is_authenticated:
        return redirect("login")
    paquete = {}
    if request.POST:
        form = AccountUpdateform(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado")
        else:
            messages.error(request, "Parece que hay un error :v")
    else:
        form  = AccountUpdateform(
            initial={
            'email':request.user.email,
            'username':request.user.username,
            }
        )
    paquete['account_form']=form
    return render(request, "perfil.html",paquete)


def R_Turista(request):
    if request.user.is_authenticated:
        if request.method == "GET":
                paquete = {'form': CreateTurista}
                return render(request,"cuestionario1.html", paquete )
        else:
            datos = request.POST
            form = CreateTurista(datos)
            if form.is_valid():
                Turi = form.save(commit=False)
                Turi.user = request.user
                Turi.save()# guarda en la base de datos
                return redirect("EnQuest", cedu= Turi.cedula)
                #return render(request, "cuestionario2.html", Turi)
                
            else:
                print(form.errors)
                paquete = {'Exiliado': 'cuestionario1' }
                return render(request,"Exilio.html", paquete )
    else:
        paquete = {'Exiliado': 'El exterior' }
        return render(request,"Exilio.html", paquete )

