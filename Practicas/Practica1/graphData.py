import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 300


ret = rrdtool.graph( "datagram.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Datagramas \n Usando SNMP y RRDtools",
                     "DEF:dataEntrada=datagram.rrd:dataEntrada:AVERAGE",
                     "DEF:dataSalida=datagram.rrd:dataSalida:AVERAGE",
                     "AREA:dataEntrada#00FF00:Datagramas de entrada",
                     "LINE3:dataSalida#0000FF:Datagramas de salida")