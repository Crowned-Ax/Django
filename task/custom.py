from models import *
from collections import Counter


class Estadisticas_por_ciudad:

    def estadisticas_Turista_Internacional(self,c):
        Turista_Internacional = Turista.objects.all().exclude(pais="colombia")
        Turista_Internacional_LastYear = [] # Turistas del ultimo año
        Turista_Internacional_PerMonth = [] # Numero de turistas por cada mes
        meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        Cantidad_PerMonth = [0,0,0,0,0,0,0,0,0,0,0,0]
        Turista_Internacional_PerMonth.append(meses)
        Turista_Internacional_PerMonth.append(Cantidad_PerMonth)

        gastos = 0

        for i in Turista_Internacional:
            temp = Cuestionario.objects.get(cuestionado=i.cedula)
            if temp.fecha_llegada.year == 2022 and temp.ciudad_destino == c: # comprobar que sea de este año
                Turista_Internacional_LastYear.append(i)
                temp2 = temp.fecha_llegada.month
                Turista_Internacional_PerMonth[1][temp2-1] +=1 #sumar los visitantes por mes
                temp3 = temp.Aprox_gasto
                gastos+= temp3

        N_Inter = Turista_Internacional_LastYear.count() # Numero de turistas en el ultimo año
        PerMonth = 0
        for j in range(12):
            PerMonth += Turista_Internacional_PerMonth[1][j]
        
        if PerMonth == 0:
            Promedio_PerMonth = 0
        else:
            Promedio_PerMonth = round((PerMonth/12),2)
        if len(Turista_Internacional_LastYear) == 0:
            Promedio_gastos = 0
        else:
            Promedio_gastos = round( (gastos/ N_Inter),2 )

        self.Numero_T_Internacional_Year = N_Inter
        self.Promedio_gastos_internacional = Promedio_PerMonth
        self.Promedio_T_por_mes_internacional = Promedio_gastos

    def estadisticas_Turista_Nacional(self,c): # segun la ciudad especificada
        Turista_Nacional = Turista.objects.filter(pais="colombia")
        Turista_Nacional_LastYear = [] # Turistas del ultimo año
        Turista_Nacional_PerMonth = [] # Numero de turistas por cada mes
        meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        Cantidad_PerMonth = [0,0,0,0,0,0,0,0,0,0,0,0]
        Turista_Nacional_PerMonth.append(meses)
        Turista_Nacional_PerMonth.append(Cantidad_PerMonth)

        gastos = 0

        for i in Turista_Nacional:
            temp = Cuestionario.objects.get(cuestionado=i.cedula)
            if temp.fecha_llegada.year == 2022 and temp.ciudad_destino == c: # comprobar que sea de este año
                Turista_Nacional_LastYear.append(i)
                temp2 = temp.fecha_llegada.month
                Turista_Nacional_PerMonth[1][temp2-1] +=1 #sumar los visitantes por mes
                temp3 = temp.Aprox_gasto
                gastos+= temp3

        N_Nacional = Turista_Nacional_LastYear.count() # Numero de turistas en el ultimo año
        PerMonth = 0
        for j in range(12):
            PerMonth += Turista_Nacional_PerMonth[1][j]
        
        if PerMonth == 0:
            Promedio_PerMonth = 0
        else:
            Promedio_PerMonth = round((PerMonth/12),2)
        if len(Turista_Nacional_LastYear) == 0:
            Promedio_gastos = 0
        else:
            Promedio_gastos = round( (gastos/ N_Nacional),2 )

        self.Numero_T_Nacional_Year = N_Nacional
        self.Promedio_gastos_nacional = Promedio_PerMonth
        self.Promedio_T_por_mes_nacional = Promedio_gastos

    def General(self,c):
        Turistas = Turista.objects.all()
        Turista_PerMonth = [] # Numero de turistas por cada mes
        meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        Cantidad_PerMonth = [0,0,0,0,0,0,0,0,0,0,0,0]
        Turista_PerMonth.append(meses)
        Turista_PerMonth.append(Cantidad_PerMonth)
        gastos = 0

        for i in Turistas:
            temp = Cuestionario.objects.get(cuestionado=i.cedula)
            if temp.fecha_llegada.year == 2022 and temp.ciudad_destino == c: # comprobar que sea de este año
                temp2 = temp.fecha_llegada.month
                Turista_PerMonth[1][temp2-1] +=1 #sumar los visitantes por mes
                temp3 = temp.Aprox_gasto
                gastos+= temp3

        if len(Turistas) == 0:
            Promedio_gastos = 0
        else:
            Promedio_gastos = round( (gastos/ len(Turistas)),2 )
        
        self.Promedio_gastos = Promedio_gastos
        self.TuristasPorMes = Turista_PerMonth

        
    def estadisticas_Lugar_Mas_Visitado(self,c):
        ls =[]
        info = Cuestionario.objects.filter(fecha_salida__year= 2022).only("destino")
        contador = Counter(info)
        first,second,third,fourth,fifth = contador.most_common()
        ls.extend([first,second,third,fourth,fifth])
        self.Lugares_mas_visitados = ls

    def __init__(self, ciudad):
        #Nacional
        self.Numero_T_Nacional_Year
        self.Promedio_gastos_nacional
        self.Promedio_T_por_mes_nacional
        #Internacional
        self.Numero_T_Internacional_Year
        self.Promedio_gastos_internacional
        self.Promedio_T_por_mes_internacional
        #General
        self.TuristasPorMes # cuantos hubo en cada mes
        self.Promedio_gastos
        self.Lugares_mas_visitados = []
        #Generar
        self.estadisticas_Turista_Internacional(ciudad)
        self.estadisticas_Turista_Nacional(ciudad)
        self.General(ciudad)