import paramiko
import sys
import os

def UploadFileAndExecute(connection,fileName):

    sftpClient = ssh.open_sftp()
    
    filen = os.path.basename(fileName)
    
    sftpClient.put(fileName, "/tmp/"+filen)
 
    ssh.exec_command("chmod a+x /tmp/" +filen)
 
    ssh.exec_command("nohup /tmp/" +filen+ " &")

if __name__ == "__main__":

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])
    	
    UploadFileAndExecute(ssh, sys.argv[4])
	
    ssh.close()
