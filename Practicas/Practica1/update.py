import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

for x in range(300):
    total_input_traffic = int(
        consultaSNMP('comunidadASR','localhost',
                     '1.3.6.1.2.1.2.2.1.11.1'))
    total_output_traffic = int(
        consultaSNMP('comunidadASR','localhost',
                     '1.3.6.1.2.1.2.2.1.11.1'))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update('unicast.rrd', valor)
    rrdtool.dump('unicast.rrd','unicast.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)