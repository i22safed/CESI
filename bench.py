#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:06:54 2017

@desc: Benchmarking on python2

@author: david
"""
import ftplib
from os import chdir, listdir, system, rename
import threading 


host = 'localhost'
user = 'david'
password = '1234'


def uploadFiles(pMon, pKill): 

    ftp = startService(host,user,password)
    createDirs(ftp)
    pMon.start()
    
    ruta = "/home/david/code/CESI/cargaPrueba/imagenesPequenas/"
    chdir(ruta)
    ftp.cwd("cargaPrueba/imagenesPequenas/")
    
    for file in listdir(ruta):
        f = open(file,'rb')
        print(ftp.storbinary('STOR '+file,f))
        f.close()
    
    pKill.start()  
    pMon.join()
    pKill.join()
    
    rename("/home/david/code/CESI/stats.txt","/home/david/code/CESI/stats1.txt")
    
    pMon.start()
    
    ruta = "/home/david/code/CESI/cargaPrueba/imagenesMedianas/"
    chdir(ruta)
    ftp.cwd("/")
    ftp.cwd("cargaPrueba/imagenesMedianas/")

    for file in listdir(ruta):
        f = open(file,'rb')
        print(ftp.storbinary('STOR '+file,f))
        f.close()

    pKill.start()  
    pMon.join()
    pKill.join()

    rename("/home/david/code/CESI/stats.txt","/home/david/code/CESI/stats2.txt")

    ruta = "/home/david/code/CESI/cargaPrueba/imagenesGrandes/"
    chdir(ruta)
    ftp.cwd("/")
    ftp.cwd("cargaPrueba/imagenesGrandes/")
   
    pMon.start()
    
    for file in listdir(ruta):
        f = open(file,'rb')
        print(ftp.storbinary('STOR '+file,f))
        f.close()
    
    pKill.start()  
    pMon.join()
    pKill.join() 
    
    rename("/home/david/code/CESI/stats.txt","/home/david/code/CESI/stats3.txt")
    
    print(endService(ftp))
    
    
def startService(host,user,password):
    
    ftp = ftplib.FTP(host) 
    ftp.set_pasv(True)
    print(ftp.login(user,password))

    return ftp 

def endService(ftp):

    print("Finalizado el servicio FTP")
    return ftp.quit()    

def createDirs(ftp):
    
    ftp.mkd("cargaPrueba")
    ftp.cwd("cargaPrueba")
    ftp.mkd("imagenesGrandes")
    ftp.mkd("imagenesMedianas")
    ftp.mkd("imagenesPequenas")
    ftp.cwd("/")
    print("-> Creadas las carpetas en el servidor")
    
def cleanFTP():
    
    ftp = startService(host,user,password)
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesGrandes")
    
    ftp.delete("*.jpg")
    ftp.delete("*.JPG")
        
    ftp.cwd("/")
    ftp.cwd("cargaPrueba")
    ftp.rmd("imagenesGrandes")
    
    ftp.cwd("imagenesMedianas")

    ftp.delete("*.jpg")
    ftp.delete("*.JPG")

    ftp.cwd("/")
    ftp.cwd("cargaPrueba")
    ftp.rmd("imagenesMedianas")
    
    ftp.cwd("/")
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesPequenas")
    
    
    ftp.delete("*.jpg")
    ftp.delete("*.JPG")
    
    ftp.cwd("/")
    ftp.cmd("cargaPrueba")
    ftp.rmd("imagenesPequenas")
    
    ftp.cwd("/")
    ftp.rmd("cargaPrueba")
    
    print("Borrada la carpeta cargaPrueba")
    endService(ftp)

def dowloadFiles():

    ftp = startService(host,user,password)
    
    pMon.start()
    
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesGrandes")

    for file in ftp.dir: 
        ftp.retrbinary('RETR '+file+'.txt',open(file+'.txt','wb').write) 
        
    ftp.cwd("/")
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesMedianas")

    for file in ftp.dir: 
        ftp.retrbinary('RETR '+file+'.txt',open(file+'.txt','wb').write) 

    ftp.cwd("/")
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesPequenas")
    
    for file in ftp.dir: 
        ftp.retrbinary('RETR '+file+'.txt',open(file+'.txt','wb').write) 
    
    pKill.start()  
    pMon.join()
    pKill.join()

    endService(ftp)

def listFiles():
    
    ftp = startService(host,user,password)
    
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesGrandes")

    ftp.dir(ftp.cwd)
        
    ftp.cwd("/")
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesMedianas")

    ftp.dir(ftp.cwd)

    ftp.cwd("/")
    ftp.cwd("cargaPrueba")
    ftp.cwd("imagenesPequenas")
    
    ftp.dir(ftp.cwd)
    
    endService(ftp)

def monitor(nombre):
    
    system('sudo docker stats > /home/david/code/CESI/stats.txt')
    
    
def kill():
    
    system('sudo kill -15 $(pidof bash)')
    
    
pMon = threading.Thread(name="mon",target=monitor)
pKill = threading.Thread(name="kill",target=kill)
uploadFiles(pMon,pKill)



  