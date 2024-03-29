import sys
import rrdtool
from  Notify import send_alert_attached
import time

ultima_lectura = int(rrdtool.last("trend.rrd"))
tiempo_final = ultima_lectura
tiempo_inicial = tiempo_final - 1800

ret = rrdtool.graphv("deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Cpu load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Uso del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",

                    "DEF:cargaCPU=trend.rrd:CPUload:AVERAGE",
                    "DEF:usoRAM=trend.rrd:storageUsed:AVERAGE",
                    #"DEF:al=trend.rrd:almacenamiento:AVERAGE",

                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",

                     "CDEF:umbral10=cargaCPU,10,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral10#FF9F00:Carga CPU mayor que 10",
                     "HRULE:10#FF0000:Umbral 10 - 5%",

                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
print (ret)

ultimo_valor=float(ret['print[0]'])
