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
    path='C:\\Users\\poaa\\Documents\\Python Scripts\\altamira_test.xml'
    tag_label='promocion'
    f = open(path,'r')
    full_file=f.read()
    promociones=Read_tag_content(full_file,tag_label)
    f.close
    for w in promociones:
#        print ('Obtenida la promoción:')
#        print(w)
        provincias=Read_tag_content(w,'provincia')
        for p in provincias:
            print(Read_tag_label(p,'provincia'))
        
    

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
    