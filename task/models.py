from django.db import models
from cuenta.models import Account

class CharLower(models.CharField):
    def __init__(self, *args, **kwargs):
        super(CharLower, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Turista(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = CharLower(max_length=255)
    edad = models.IntegerField()
    pais = CharLower(max_length=255)
    form_pago = [('D','Debito'),('C','Credito'),('E','Efectivo')]
    forma_pago = models.CharField(max_length=1, choices=form_pago)
    correo = models.CharField(max_length=255)
    telefono = models.IntegerField()

    class Meta:
        verbose_name = "Turista"
        verbose_name_plural = "Turista"

    def __str__(self):
        return self.nombre


class Cuestionario(models.Model):
    agente = models.ForeignKey(Account, on_delete=models.CASCADE)
    cuestionado = models.ForeignKey(Turista, on_delete=models.CASCADE)
    acompanante = models.BooleanField()
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    ciudad_destino = CharLower(max_length=255)
    destino = CharLower(max_length=255)
    transportes = [("Carro","carro"),("Moto","moto"),("vehiculo alquilado","vehiculo alquilado"),("Bus","bus"),("Taxi","taxi") ]
    T_transporte = models.CharField(max_length=20,choices=transportes)
    Aprox_gasto = models.IntegerField()
    equipo = models.TextField()
    
    class Meta:
        verbose_name = "Cuestionario"
        verbose_name_plural = "Cuestionarios"

    def __str__(self):
        return str(self.id)
