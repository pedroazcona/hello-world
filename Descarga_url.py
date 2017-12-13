# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:05:24 2017

@author: poaa
"""


import urllib
import time
 
archivoDescargar = "http://www.altamirainmuebles.com/xml/sareb01_obranueva.xml"
archivoGuardar = "C:\\Users\\poaa\\Documents\\Python Scripts\\sareb01_obranueva.xml"
 
now = time.time()

try: 
    descarga=urllib.request.urlopen(archivoDescargar)
#descarga = urllib.request(archivoDescargar)

    ficheroGuardar=open(archivoGuardar,'wb')
    ficheroGuardar.write(descarga.read())
    ficheroGuardar.close()
 
    elapsed = time.time() - now
 
    print ("Descargado el archivo: %s en %0.3fs" % (archivoDescargar,elapsed))

except HTTPError as e:
    print ('Error HTTP:', e.code, archivoDescargar)