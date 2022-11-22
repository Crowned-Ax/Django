from task.models import *
from collections import Counter


class Estadisticas_por_ciudad:

    """Nacional
    Numero_T_Nacional_Year
    Promedio_gastos_nacional
    Promedio_T_por_mes_nacional
    #Internacional
    Numero_T_Internacional_Year
    Promedio_gastos_internacional
    Promedio_T_por_mes_internacional
    #General
    TuristasPorMes # cuantos hubo en cada mes
    meses -_- toco
    self.Cantidad_PerMonth  -_- 
    Promedio_gastos_G
    Lugares_mas_visitados = []"""

    def __init__(self, ciudad):
        #Generar
        self.estadisticas_Turista_Internacional(ciudad)
        self.estadisticas_Turista_Nacional(ciudad)
        self.General(ciudad)
        self.estadisticas_Lugar_Mas_Visitado()
        transporte = self.estadisticas_Transporte_Mas_Usado()
        self.tabla3 = zip(self.Lugares_mas_visitados,self.Most_vehiculo)

    def estadisticas_Turista_Internacional(self,c):
        Turista_Internacional = Turista.objects.all().exclude(pais="colombia")
        if Turista_Internacional.exists():
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

            N_Inter = len(Turista_Internacional_LastYear) # Numero de turistas en el ultimo año
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
            self.Promedio_gastos_internacional = Promedio_gastos
            self.Promedio_T_por_mes_internacional = Promedio_PerMonth
        else:
            self.Numero_T_Internacional_Year = 0
            self.Promedio_gastos_internacional = 0
            self.Promedio_T_por_mes_internacional = 0

    def estadisticas_Turista_Nacional(self,c): # segun la ciudad especificada
        Turista_Nacional = Turista.objects.filter(pais="colombia")
        if Turista_Nacional.exists():
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

            N_Nacional = len(Turista_Nacional_LastYear) # Numero de turistas en el ultimo año
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
            self.Promedio_gastos_nacional = Promedio_gastos
            self.Promedio_T_por_mes_nacional = Promedio_PerMonth
        else:
            self.Numero_T_Nacional_Year = 0
            self.Promedio_gastos_nacional = 0
            self.Promedio_T_por_mes_nacional = 0

    def General(self,c):
        Turistas = Turista.objects.all()
        self.meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        self.Cantidad_PerMonth = [0,0,0,0,0,0,0,0,0,0,0,0]

        if Turistas.exists():
            Turista_PerMonth = [] # Numero de turistas por cada mes
            Turista_PerMonth.append(self.meses)
            Turista_PerMonth.append(self.Cantidad_PerMonth)
            gastos = 0

            for i in Turistas:
                temp = Cuestionario.objects.get(cuestionado=i.cedula)
                if temp.fecha_llegada.year == 2022 and temp.ciudad_destino == c: # comprobar que sea de este año
                    temp2 = temp.fecha_llegada.month
                    Turista_PerMonth[1][temp2-1] +=1 #sumar los visitantes por mes
                    print("mes "+ str(temp2))
                    temp3 = temp.Aprox_gasto
                    gastos+= temp3

            if Turistas.count() == 0:
                Promedio_gastos = 0
            else:
                Promedio_gastos = round( (gastos/ len(Turistas)),2 )
            
            self.Promedio_gastos_G = Promedio_gastos
            self.TuristasPorMes = Turista_PerMonth
        else:
            self.Promedio_gastos_G = 0
            self.TuristasPorMes = 0

        
    def estadisticas_Lugar_Mas_Visitado(self):
        ls =[]
        info = Cuestionario.objects.filter(fecha_salida__year= 2022).only("destino")
        info2 = []
        for j in info:
            info2.append(j.destino)
        contador = Counter(info2)
        
        p = len(contador)
        if p == 1:
            first = contador.most_common()
            ls.append(first[0][0])
        elif p == 2:
            first,second = contador.most_common()
            ls.extend([first[0],second[0]])
        elif p == 3:
            first,second,third = contador.most_common()
            ls.extend([first[0],second[0],third[0]])
        elif p == 4:
            first,second,third,fourth = contador.most_common()
            ls.extend([first[0],second[0],third[0],fourth[0]])
        elif p == 5:
            first,second,third,fourth,fifth = contador.most_common()
            ls.extend([first[0],second[0],third[0],fourth[0],fifth[0]])

        self.Lugares_mas_visitados = ls

    def estadisticas_Transporte_Mas_Usado(self):
        ls =[]
        info = Cuestionario.objects.filter(fecha_salida__year= 2022).only("destino")
        info2 = []
        for j in info:
            info2.append(j.T_transporte)
        contador = Counter(info2)
        p = len(contador)
        if p == 1:
            first = contador.most_common()
            ls.append(first[0])
        elif p == 2:
            first,second = contador.most_common()
            ls.extend([first[0],second[0]])
        elif p == 3:
            first,second,third = contador.most_common()
            ls.extend([first[0],second[0],third[0]])
        elif p == 4:
            first,second,third,fourth = contador.most_common()
            ls.extend([first[0],second[0],third[0],fourth[0]])
        elif p == 5:
            first,second,third,fourth,fifth = contador.most_common()
            ls.extend([first[0],second[0],third[0],fourth[0],fifth[0]])

        self.Most_vehiculo = ls

