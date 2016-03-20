import os
from os.path import dirname
from os import listdir


if not os.path.exists("clone"):    
    os.mkdir("clone");   

fo = open("payload.txt", "wb")
fo.write('I am a quine XD.')
fo.close()

fo = open("replicate.py", "wb")
fo.write('from sys import argv\n\
import os\n\
script=argv\n\
name=str(script[0])\n\
print name\n\
cmd= \'start payload.txt\'\n\
os.system(cmd)\n\
if not os.path.exists(\'clone\'): os.mkdir(\'clone\')\n\
os.system(r"copy payload.txt clone")\n\
os.system(r"copy replicate.py clone")\n\
os.system(r"copy 1.Click.bat clone")\n\
os.system("1.Initiate.py 1")\
')
fo.close()

    
print 'Author: Frank Stajano (fstajano@orl.co.uk)'
l='l=%s;print l%%`l`'
print l%`l`


os.system("replicate.py 1")




