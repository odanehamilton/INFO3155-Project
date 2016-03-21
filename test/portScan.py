import optparse
from socket import *
import os
import sys
import threading
import Queue
import time

#...List of common ports and their descriptions...#
common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "67": "DHCP",
    "80": "HTTP",
    "110": "POP3",
    "139": "netBIOS",
    "143": "IMAP",
    "194": "IRC",
    "443": "HTTPS",
    "465": "Cisco Protocol",
    "993": "IMAPS",
    "995": "POP3S",
    "3306": "MySQL",
    "25565": "Minecraft"
}

#############################################################################################################################################
#...function which check information from banner received against list of known vulnerabilites...#

def vulcheck(banner):
    path = ''
    keep = open(path+"vul_list.txt", 'r')
    vlst = []
    for line in keep.readlines():
        line = line.strip('\n')
        line = line.strip('\t')
        if line in banner:
            vlst += line
            print ' [+] ' + line + ' is vulnerable'
            print '\n'
    keep.close()
#############################################################################################################################################
#...function which gets the banner by connect to a targethost and port...#
    
def getBanner(targetHost, targetPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((targetHost, int(targetPort)))
        try:
            #conn.send("HACKER")
            banner = conn.recv(1024)
        except:
            conn.send("HEAD / HTTP/1.0\r\n\r\n")
            banner = conn.recv(1024)
        return banner
    except:
        return
    
#############################################################################################################################################
#...function to connect to a given host and port...#
    
def conn(targetHost, targetPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((targetHost, targetPort))
        if str(targetPort) in common_ports:
            print ('[+] Connection to ' + targetHost + " port {} ({})".format(str(targetPort), common_ports[str(targetPort)]) + ' successful!')
        else:
            print '[+] Connection to ' + targetHost + ' port ' + str(targetPort) + ' successful!'
            
    except Exception, e:
        print '[-] Connection to ' + targetHost + ' port ' + str(targetPort) + ' failed: ' + str(e)
    finally:
        conn.close()

#############################################################################################################################################
#...main function which parses the inputs given. scanning will be done for 1 host or multiple hosts with 1 port, many ports or...#
#...a selection of ports separated by commas...#
        
def main():
    parser = optparse.OptionParser("%prog -t <target host(s)> -p <target port(s)>")
    parser.add_option('-t', dest='targetHosts', type='string', help='Specify the target host(s); Separate them by commas')
    parser.add_option('-p', dest='targetPorts', type='string', help='Specify the target port(s); Separate them by commas or range of port(s) separated by a hyphen')

    (options, args) = parser.parse_args()
    if (options.targetHosts == None) | (options.targetPorts == None):
        print parser.usage
        exit(0)


    elif "-" in str(options.targetPorts):
        targetHosts = str(options.targetHosts).split(',')
        targetPorts = str(options.targetPorts).split('-')
        targetPorts = range(int(targetPorts[0]), int(targetPorts[1])+1)

    else:
        targetHosts = str(options.targetHosts).split(',')
        targetPorts = str(options.targetPorts).split(',')

    setdefaulttimeout(5)
    
    start_time = time.time()
    
    for targetHost in targetHosts:
        for targetPort in targetPorts:
            conn(targetHost, int(targetPort))
        print ''

    for targetHost in targetHosts:
        for targetPort in targetPorts:
            banner = str(getBanner(targetHost, targetPort))
            print ' \n===== Banner information for ' + targetHost + ' on port: ' + str(targetPort) + ' =====\n'
            print banner
            print  '============================================================ '
            print ''
            print ''
            vulcheck(banner)
            #toFile(banner)


        
    end_time = time.time()
    print("Done! Time taken to complete: {:.3f} seconds.".format(end_time - start_time))
    print '=' * 60


#############################################################################################################################################        

if __name__ == '__main__':
 main()
