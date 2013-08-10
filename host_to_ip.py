# coding: utf-8

import sys
import socket


def host_to_ip(host):
    '''get the host with host'ip 
    '''
    try:
        ip = socket.gethostbyname(host)
        return ip
        
        #other chiose
        #myaddr = socket.getaddrinfo(host,'http')[0][4][0]
        #result = socket.gethostbyaddr(myaddr)
        #return result[2][0]
    except:
        return False
 
if __name__=="__main__":
    print host_to_ip("baidu.com")

