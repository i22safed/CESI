#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:38:12 2017

@author: david
"""


def formatFile():
    
    ruta = "/home/david/code/CESI/"
    
    file = open(ruta+'formatted.txt','r')
    aux = open(ruta+'formatted1.txt','w')
    
    for line in file: 
        if '.' in line: 
            aux.write(line.replace('.',','))
        
    file.close()
    aux.close()
    
formatFile()