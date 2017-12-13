# -*- coding: utf-8 -*-
"""
Invisible friend
Created on Fri Dec  1 08:47:03 2017
Simula el sorteo del amigo invisible
@author: poaa
"""
import random
def amigo_invisible():
    error= False
    couples =[('Pedro', 'Chus'),('Manolo', 'Makechu'), ('Elena','Alberto'),];
#    couples=[]
    friends =['Pili','Pedro', 'Chus','Manolo', 'Makechu', 'Elena','Alberto'];
    pelotillas =['Pili','Pedro', 'Chus','Manolo', 'Makechu', 'Elena','Alberto'];
    for i in friends:
        k= random.randrange(len(pelotillas))
        if pelotillas[k]==i:
            error=True
            break
        if (i,pelotillas[k]) in couples or (pelotillas[k],i) in couples:
             error=True
             break
#        resultado = 'A '+ i + ' le toca ' + pelotillas[k]
#        print(resultado)
        pelotillas.remove(pelotillas[k])
    if (error):
       return(1)
    else:
       return(0)

    
def execute_simulation(Rango):
    OK=0
    KO=0
    for i in range(Rango):
        if(amigo_invisible())==0:
            OK=OK+1
        else:
            KO=KO+1
    print('%OK:' + str(OK*100/(OK+KO)))