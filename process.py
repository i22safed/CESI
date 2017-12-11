#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:42:24 2017

@author: david
"""

from os import system
import threading
import time 


def monitor(i):
    print("antes1")
    system('sudo docker stats > /home/david/code/CESI/'+str(i)+'.txt')
    print("despues1")
    
def kill():
    print("antes2")
    system('sudo kill -15 $(pidof sudo)')
    print("despues2")

def getStats(i):
    
    print("Hasta aqui llega")
    pMon = threading.Thread(name="mon",target=monitor,args=(i, ))
    pKill = threading.Thread(name="kill",target=kill)
    pMon.start()
    time.sleep(0.5)
    pKill.start()
    pMon.join()
    pKill.join()
    

