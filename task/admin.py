from django.contrib import admin
from task.models import *
from cuenta.models import Account

@admin.register(Turista)
class TuristaAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Cuestionario)
class CuestionarioAdmin(admin.ModelAdmin):
    pass
