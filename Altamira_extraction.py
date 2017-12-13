# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:04:08 2017

@author: poaa
"""

import re

def Find(expr,text):
     m=re.findall(expr,text)
     return m

def Read_tag_value(full_file,tag_label):
    tag_value_dic ={}
    tag_values=Find(r'<'+ tag_label +'>\w+</'+ tag_label +'>',full_file)
    for tag_value in tag_values:
        tag_value = tag_value.replace('<'+ tag_label +'>','')
        tag_value = tag_value.replace('</'+ tag_label +'>','')
        tag_value = tag_value.upper()
        if not tag_value: continue
        if not tag_value in tag_value_dic:
            tag_value_dic[tag_value] = 1
        else:
            tag_value_dic[tag_value] += 1
    sorted_tags = sorted([(n, w) for w, n in tag_value_dic.items()], reverse=True)
    print('La lista de '+ tag_label +' es: ', sorted_tags)
    
def Read_tag_list(full_file,tag_label):
    tag_value_dic ={}
    tag_values=Find(r'<'+ tag_label +'>',full_file)
    for tag_value in tag_values:
        tag_value = tag_value.replace('<','')
        tag_value = tag_value.replace('>','')
        tag_value = tag_value.upper()
        if not tag_value: continue
        if not tag_value in tag_value_dic:
            tag_value_dic[tag_value] = 1
        else:
            tag_value_dic[tag_value] += 1
    sorted_tags = sorted([(n, w) for w, n in tag_value_dic.items()], reverse=True)
    print('La lista de '+ tag_label +' es: ', sorted_tags)

def main():
    path='C:\\Users\\poaa\\Documents\\Python Scripts\\sareb01_segundamano.xml'
    f = open(path,'r')
    full_file=f.read()
    promociones=Read_tag_content(full_file,'promocion')
    f.close
    for w in promociones:
#        print ('Obtenida la promoción:')
#        print(w)
        cod_promo=Read_tag_content(w,'codigo_promocion')[0]
        print('*****************************************************************')
        print('Codigo Promo:', Read_tag_label(cod_promo,'codigo_promocion'))
        propietario=Read_tag_content(w,'propietario')[0]
        print('propietario: ',Read_tag_label(propietario,'propietario'))
        provincia=Read_tag_content(w,'provincia')[0]
        print('Provincia: ',Read_tag_label(provincia,'provincia'))
        localidad=Read_tag_content(w,'localidad')[0]
        print('localidad: ',Read_tag_label(localidad,'localidad'))
        inmuebles=Read_tag_content(w,'inmueble')
        for inmueble in inmuebles:
            print ('Obtenidos los inmuebles:')
#            print(inmueble)
            id_inmueble=Read_tag_content(inmueble,'id_inmueble')[0]
            referencia=Read_tag_content(inmueble,'referencia')[0]
            tipo=Read_tag_content(inmueble,'tipo')[0]
            Direccion_inmueble=Read_tag_content(inmueble,'Direccion_inmueble')[0]
            precio_venta=Read_tag_content(inmueble,'precio_venta')[0]
            precio_alquiler=Read_tag_content(inmueble,'precio_alquiler')[0]
#           if tipo.strip()=='<tipo>Piso</tipo>':
            print('id_inmueble: ',Read_tag_label(id_inmueble,'id_inmueble'))
            print('Referencia: ',Read_tag_label(referencia,'referencia'))
            print('tipo: ',Read_tag_label(tipo,'tipo'))
            print('Direccion_inmueble: ',Read_tag_label(Direccion_inmueble,'Direccion_inmueble'))
            print('Precio Venta: ',Read_tag_label(precio_venta,'precio_venta'))
            print('Precio Alquiler: ',Read_tag_label(precio_alquiler,'precio_alquiler'))
        print('-----------------------------------------------------------------')
        
    

def Read_tag_content(full_file,tag_label):
    tag_content = []
    tag_end=''
    flag_guardar=False
    i=0
    for line in re.split(r'\n',full_file):
        tag=Find(r'<'+ tag_label +'>',line)
        if tag : 
            flag_guardar=True
            tag_content.append('')
        if flag_guardar:
            tag_content[i]= tag_content[i] + line + '\n'
        tag_end=Find(r'</'+ tag_label +'>',line)
        if tag_end: 
            i +=1
            tag_end=''
            flag_guardar=False
    return tag_content

def Read_tag_label(texto,tag):
    value = texto.replace('<'+tag+ '>','')
    value = value.replace('</'+tag+ '>','')
    return value

if __name__ == '__main__':
    main()