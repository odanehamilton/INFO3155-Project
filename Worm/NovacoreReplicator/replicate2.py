#NOVACORE

from sys import argv
import os
import Tkinter
from Tkinter import *
import resource
import subprocess

script=argv
name=str(script[0])
currDirectory= os.path.dirname(name) 
print name
print currDirectory

fo = open("payload.txt", "wb")
fo.write('I am a quine XD.\n I was created by Novacore\n')
fo.close()

        
cmd= 'open payload.txt'
os.system(cmd)

for i in range(1,3):
    os.system(cmd)
    folder=currDirectory+'/clone'+str(i)
    print folder
    if not os.path.exists(folder):
        os.mkdir(folder)
     
    os.system(r"cp "+name+" "+folder)
    os.system(r"cp worm.py "+folder)
    os.system(r"cp payload.txt "+folder)
    os.system(r"cat payload.txt "+folder)

##root = Tk()
##root.title('Novacore worm')
##Label(text='  See you soon!!!!!!!  ').pack(pady=15)


##exit()
