import rrdtool
ret = rrdtool.create("datagram.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:dataEntrada:COUNTER:120:U:U",
                     "DS:dataSalida:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:6:5",
                     "RRA:AVERAGE:0.5:1:20")
if ret:
    print (rrdtool.error())