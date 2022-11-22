from django.forms import ModelForm
from .models import *
from django import forms

class CreateTurista(ModelForm):
    class Meta:
        model = Turista
        fields = ["cedula","nombre","edad","pais","forma_pago", "correo","telefono"]
        labels = {"pais":"pais de procedencia", "correo": "correo electronico"}

class CreateCuestionario(ModelForm):
    class Meta:
        model = Cuestionario
        fields = ["acompanante","fecha_llegada","fecha_salida","ciudad_destino","destino","T_transporte","Aprox_gasto","equipo"]
        labels = {
            "acompanante": "¿Viene con acompañante(s)?",
            "fecha_llegada": "¿Cuando partio para este viaje?" ,
            "fecha_salida": "¿cuando piensa volver o terminar este viaje?",
            "T_transporte":"¿Que tipo de transporte utiliza?",
            "Aprox_gasto": "¿Cuanto ha gastado aproximadamente en este viaje?",
            "equipo": "¿que tipo de cosas trajo para su viaje?",
        }
        widgets = {
            'acompanante':forms.CheckboxInput(),
            'fecha_llegada':forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'fecha_salida':forms.DateInput(attrs={'class':'form-control' , 'type': 'date'}),
        }
