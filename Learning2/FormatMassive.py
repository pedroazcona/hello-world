# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:03:28 2017

@author: poaa

El script selecciona las columnas en selectedColumns y las formatea al tamaño columSize. 
ColumnSize(i)=0 --> No se modifica la columna.
ColumnSize(i)=20 --> La columna se rellena con espacios hasta llegar a tamño 20.
Notar que la columna se rellena con espacios, pero si supera 20, no se corta.
"""
separadorEntrada = '|'
separadorSalida = ','
selectedColumns=[0,2,3]
columnSize=[0,0,12]
infile=open(r'C:\Users\poaa\Documents\Python Scripts\Learning2\Fichero1.txt','r')
outfile=open(r'C:\Users\poaa\Documents\Python Scripts\Learning2\Massive1.txt','w+')
for a in infile:
     c=a.split(sep=separadorEntrada)
     outputLine=''
     for i in range(0,len(selectedColumns)):
#        print(i)
         outputLine=outputLine + c[selectedColumns[i]].ljust(columnSize[i]) +separadorSalida
     outputLine=outputLine + '\n'
     outfile.write(outputLine)
infile.close
outfile.close