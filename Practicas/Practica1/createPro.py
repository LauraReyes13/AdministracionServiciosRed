import rrdtool
ret = rrdtool.create("protocolo.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:proEntrada:COUNTER:120:U:U",
                     "DS:proSalida:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:6:5",
                     "RRA:AVERAGE:0.5:1:20")
if ret:
    print (rrdtool.error())