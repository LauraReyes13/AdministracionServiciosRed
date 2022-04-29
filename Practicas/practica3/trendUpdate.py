import time
import rrdtool
from getSNMP import consultaSNMP
comunidad = "ComunidadASR"
host = "localhost"


while 1:
    carga_CPU = int(consultaSNMP(comunidad,host,'1.3.6.1.2.1.25.3.3.1.2.196608'))
    storage_used = int(consultaSNMP(comunidad,host,'1.3.6.1.2.1.25.2.3.1.6.1'))
    valor = "N:" + str(carga_CPU) + ":" + str(storage_used)
    print (valor)
    rrdtool.update('trend.rrd', valor)
    rrdtool.dump('trend.rrd','trend.xml')
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
