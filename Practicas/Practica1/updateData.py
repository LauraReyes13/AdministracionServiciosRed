import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

for x in range(300):
    total_input_traffic = int(
        consultaSNMP('comunidadASR','localhost',
                     '1.3.6.1.2.1.7.1.0'))
    total_output_traffic = int(
        consultaSNMP('comunidadASR','localhost',
                     '1.3.6.1.2.1.7.1.0'))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update('datagram.rrd', valor)
    rrdtool.dump('datagram.rrd','datagram.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)