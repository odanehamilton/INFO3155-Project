import os
from os.path import dirname
from os import listdir

newpath = r"C:\Users\Jeremy-Dane\Desktop"

folder='\Hello'
directory=newpath+folder
if not os.path.exists(directory):    
    os.mkdir(directory);
    
origin= os.path.dirname(os.path.realpath(__file__))

os.system(r"copy replicator.py"+ directory)
    

    
##if os.path.exists(directory):
fo = open(directory+"\payload.txt", "wb")
fo.write('I am a quine.')
fo.close()

fr = open(directory+"\launch.bat", "wb")
fr.write('replicator.py %*')
fr.close()

    
print 'Author: Frank Stajano (fstajano@orl.co.uk)'

l='l=%s;print l%%`l`'
print l%`l`

parent=os.path.dirname(os.path.dirname(directory))

print os.listdir(directory)
##print os.listdir(parent)

os.system("replicator.py 1")




