#NOVACORE

from sys import argv
import os
import Tkinter
from Tkinter import *
import resource
import subprocess

script=argv
name=str(script[0])

print "Before\n"
print resource.getrusage(1)
print resource.getrusage(0)

print '\nProcess ID: '+ str(os.getpid())
print os.system("ps u -p %d | awk '{sum=sum+$6}; END {print sum/1024}'" %os.getpid())


fo = open("payload.txt", "wb")
fo.write('I am a quine XD.\n I was created by Novacore')
fo.close()


cmd= 'start payload.txt'
for i in range(1,5):
    folder='clone'+str(i)
    os.system(cmd)
    if not os.path.exists(folder):
        os.mkdir(folder)
        os.system(r"copy payload.txt "+folder)
        os.system(r"copy replicate.py"+folder)
        os.system(r"copy 1.Click.bat "+folder)
       
print "\n\nAfter\n"
print resource.getrusage(1)
print resource.getrusage(0)

print '\nProcess ID: '+ str(os.getpid())
print os.system("ps u -p %d | awk '{sum=sum+$6}; END {print sum/1024}'" %os.getpid())
##print os.system("ps u -p "+str(os.getpid())+" | awk '{sum=sum+$6}; END {print sum/1024}'")
print "\n\n"

list = []
 
# create a list with ten million elements
 
for i in range(0,10000000):
    list.append('abcdefg')
    if len(list) % 1000000 == 0:
        print(len(list), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

print " \nM E M O R Y   U S A G E \n"
print "Process"
rusage_denom = 1024.
if sys.platform == 'darwin':
# ... it seems that in OSX the output is different units ...
    rusage_denom = rusage_denom * rusage_denom
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
print mem
print "\n"

print "Subprocess"
out = subprocess.Popen(['ps', 'v', '-p', str(os.getpid())],
stdout=subprocess.PIPE).communicate()[0].split(b'\n')
vsz_index = out[0].split().index(b'RSS')
memor = float(out[1].split()[vsz_index]) / 1024
print memor

print '\nMemory usage: %s (kb)' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

root = Tk()
root.title('Novacore worm')
Label(text='  See you soon!!!!!!!  ').pack(pady=15)


##exit()
