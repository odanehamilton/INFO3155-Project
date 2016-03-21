from sys import argv
import os

script=argv
name=str(script[0])
print name

newpath = r"/home/ubuntu/workspace"
folder='/Hello'
directory=newpath+folder
if not os.path.exists(directory):  
    os.mkdir(directory);

payload= directory+"/payload.txt"

cmd= 'start'+payload
os.system(cmd)

newFolder=directory+"\clone"
if not os.path.exists(directory):
    os.mkdir(newFolder)

subprocess.call("cp", "p")
#os.system(r"copy payload.txt "+ newFolder)
#os.system(r"copy " + name + newFolder)
#os.system(r"copy launch.bat "+ newFolder)

