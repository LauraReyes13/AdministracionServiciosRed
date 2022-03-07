import os
import img2pdf

exec(open("create.py").read())
exec(open("createData.py").read())
exec(open("createICMP.py").read())
exec(open("createPro.py").read())
exec(open("createSeg.py").read())
exec(open("update.py").read())
exec(open("updateData.py").read())
exec(open("updateICMP.py").read())
exec(open("updatePro.py").read())
exec(open("updateSeg.py").read())
exec(open("graph.py").read())
exec(open("graphData.py").read())
exec(open("graphICMP.py").read())
exec(open("graphPro.py").read())
exec(open("graphSeg.py").read())


imagenes_jpg = [archivo for archivo in os.listdir('./') if archivo.endswith(".png")]

with open("documento.pdf", "wb") as documento:
	documento.write(img2pdf.convert(imagenes_jpg))