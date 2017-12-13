# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:35:56 2017
Cambiamos en todos los CD el artista de Eros Ramazzotti a Eros Verdaderos
@author: poaa
"""
import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\poaa\Documents\Python Scripts\Learning2\TestFiles\cd_catalog.xml')
root = tree.getroot()
print (root)
for CD in root.findall('cd'):
    YEAR = CD.find('YEAR').text
    ARTIST_T=CD.find('ARTIST').text
    ARTIST=CD.find('ARTIST')
    print(ARTIST_T, YEAR)
    if ARTIST_T =='Eros Ramazzotti':
        ARTIST.text='Eros Verdaderos'
        tree.comment='Eros es'
tree.write(r'C:\Users\poaa\Documents\Python Scripts\Learning2\TestFiles\output.xml')
