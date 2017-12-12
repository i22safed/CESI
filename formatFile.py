#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:38:12 2017

@author: david
"""


def formatFile():
    
    ruta = "/home/david/code/CESI/"
    
    file = open(ruta+'1.txt','r')
    aux = open(ruta+'formatted.txt','w')
    
    for line in file: 
        if 'cd91dce2a414' in line: 
            aux.write(line)
        
    file.close()
    aux.close()
    
formatFile()