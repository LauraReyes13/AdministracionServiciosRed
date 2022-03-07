import rrdtool
ret = rrdtool.create("segmentos.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:segEntrada:COUNTER:120:U:U",
                     "DS:segSalida:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:6:5",
                     "RRA:AVERAGE:0.5:1:20")
if ret:
    print (rrdtool.error())