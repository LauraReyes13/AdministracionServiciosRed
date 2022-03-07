import rrdtool
ret = rrdtool.create("icmp.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:icmpEntrada:COUNTER:120:U:U",
                     "DS:icmpSalida:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:6:5",
                     "RRA:AVERAGE:0.5:1:20")
if ret:
    print (rrdtool.error())