import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 300


ret = rrdtool.graph( "icmp.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Unicast \n Usando SNMP y RRDtools",
                     "DEF:icmpEntrada=icmp.rrd:icmpEntrada:AVERAGE",
                     "DEF:icmpSalida=icmp.rrd:icmpSalida:AVERAGE",
                     "AREA:icmpEntrada#00FF00:ICMP de entrada",
                     "LINE3:icmpSalida#0000FF:ICMP de salida")