import rrdtool
ret = rrdtool.create("trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload:GAUGE:600:U:U",
                     "DS:storageUsed:GAUGE:600:U:U",
                     "RRA:AVERAGE:0.5:1:1000")
if ret:
    print (rrdtool.error())
