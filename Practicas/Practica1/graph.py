import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 300


ret = rrdtool.graph( "unicast.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Unicast \n Usando SNMP y RRDtools",
                     "DEF:ucEntrada=unicast.rrd:ucEntrada:AVERAGE",
                     "AREA:ucEntrada#00FF00:Unicast de entrada")
