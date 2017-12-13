# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:39:05 2017

@author: poaa
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:04:08 2017

@author: poaa
"""

import re
import urllib.request
import time

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

def gen_cvs(archivoDescargar):

    archivo_xml=archivoDescargar.split('/')[-1]
    archivo_csv=archivo_xml.split('.')[0]+'.csv'
    archivoGuardar = "C:\\Users\\poaa\\Documents\\Python Scripts\\"+archivo_xml
    
    
    now = time.time()

    try: 
        descarga=urllib.request.urlopen(archivoDescargar)
#descarga = urllib.request(archivoDescargar)
        ficheroGuardar=open(archivoGuardar,'wb')
        ficheroGuardar.write(descarga.read())
        ficheroGuardar.close()
 
        elapsed = time.time() - now
 
        print ("Descargado el archivo: %s en %0.3fs" % (archivoDescargar,elapsed))

        path_out="C:\\Users\\poaa\\Documents\\Python Scripts\\"+archivo_csv
        generate_cvs(archivoGuardar, path_out)

    except HTTPError as e:
        print ('Error HTTP:', e.code, archivoDescargar)
    
def generate_cvs(path_in, path_out):
    f = open(path_in,'r')
    r = open(path_out,'w')
    full_file=f.read()
    promociones=Read_tag_content(full_file,'promocion')
    f.close
    r.write("Código Promo;Propietario;Provincia;Localidad;Calle;Número;Cp;Id_Inmueble;Referencia;Tipo;PrecioVentaPúblico;PrecioAlquiler;\n")
    for w in promociones:
#        print ('Obtenida la promoción:')
#        print(w)
        cod_promo=Read_tag_content(w,'codigo_promocion')[0]
        Cod=Read_tag_label(cod_promo,'codigo_promocion').split()[0]
        propietario=Read_tag_content(w,'propietario')[0]
        Prop=Read_tag_label(propietario,'propietario').split()[0]
        provincia=Read_tag_content(w,'provincia')[0]
        Prov=Read_tag_label(provincia,'provincia').split()[0]
        localidad=Read_tag_content(w,'localidad')[0]
        Loc=Read_tag_label(localidad,'localidad').split()[0]
        calle=Read_tag_content(w,'Calle')[0]
        Ca=Read_tag_label(calle,'Calle').strip()
        numero=Read_tag_content(w,'Numero')[0]
        Num=Read_tag_label(numero,'Numero').split()[0]
        cp=Read_tag_content(w,'cp')[0]
        Cp=Read_tag_label(cp,'cp').split()[0]

        inmuebles=Read_tag_content(w,'inmueble')
        for inmueble in inmuebles:
#            print ('Obtenidos los inmuebles:')
#            print(inmueble)
            id_inmueble=Read_tag_content(inmueble,'id_inmueble')[0]
            referencia=Read_tag_content(inmueble,'referencia')[0]
            tipo=Read_tag_content(inmueble,'tipo')[0]
#            calle=Read_tag_content(inmueble,'calle')[0]
            precio_venta=Read_tag_content(inmueble,'precio_venta')[0]
            precio_alquiler=Read_tag_content(inmueble,'precio_alquiler')[0]
#           if tipo.strip()=='<tipo>Piso</tipo>':
            Id_in=Read_tag_label(id_inmueble,'id_inmueble').split()[0]
            Ref=Read_tag_label(referencia,'referencia').split()[0]
            Tip=Read_tag_label(tipo,'tipo').split()[0]
#            Call=Read_tag_label(calle,'calle').split()[0]
            Pvp=Read_tag_label(precio_venta,'precio_venta').split()[0]
            Paq=Read_tag_label(precio_alquiler,'precio_alquiler').split()[0]
            Line_csv='"'+Cod+'";"'+Prop+'";"'+Prov+'";"'+Loc+'";"'+Ca+'";"'+Num+'";"'+Cp+'";"'+Id_in+'";"'+Ref+'";"'+Tip+'";"'+Pvp+'";"'+Paq+'";'
            r.write(Line_csv+'\n')
    r.close
        
    

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
    if not tag_content:
        tag_content.append('?')
    return tag_content

def Read_tag_label(texto,tag):
    value = texto.replace('<'+tag+ '>','')
    value = value.replace('</'+tag+ '>','')
    return value

def main():
    Url = "http://www.altamirainmuebles.com/xml/sareb01_obranueva.xml"
    gen_cvs(Url)
    Url = "http://www.altamirainmuebles.com/xml/sareb01_segundamano.xml"
    gen_cvs(Url)
    Url = "http://www.altamirainmuebles.com/xml/sareb01_obranueva_delta.xml"
    gen_cvs(Url)
    Url = "http://www.altamirainmuebles.com/xml/sareb01_segundamano_delta.xml"
    gen_cvs(Url)


if __name__ == '__main__':
    main()