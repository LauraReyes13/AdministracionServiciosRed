import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 300


ret = rrdtool.graph( "protocolo.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Protocolo IPV4 \n Usando SNMP y RRDtools",
                     "DEF:proEntrada=protocolo.rrd:proEntrada:AVERAGE",
                     "DEF:proSalida=protocolo.rrd:proSalida:AVERAGE",
                     "AREA:proEntrada#00FF00:IPV4 de entrada",
                     "LINE3:proSalida#0000FF:IPV4 de salida")