import rrdtool
ret = rrdtool.create("unicast.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:ucEntrada:COUNTER:120:U:U",
                     "DS:ucSalida:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:6:5",
                     "RRA:AVERAGE:0.5:1:20")
if ret:
    print (rrdtool.error())
