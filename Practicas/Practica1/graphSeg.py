import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 300


ret = rrdtool.graph( "segmentos.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Unicast \n Usando SNMP y RRDtools",
                     "DEF:segEntrada=segmentos.rrd:segEntrada:AVERAGE",
                     "DEF:segSalida=segmentos.rrd:segSalida:AVERAGE",
                     "AREA:segEntrada#00FF00:Sementos de entrada",
                     "LINE3:segSalida#0000FF:Segmentos de salida")