# coding: utf-8

import csv
import time
from alexa_api import alexa_api
from host_to_ip import host_to_ip
from ip_to_city import ip_to_city
from dblib import add_top_hosts,add_subdomain,add_china_hosts
from subdomain import get_subdomain
import gevent
import random
import signal
from gevent import Timeout
from gevent import monkey
monkey.patch_all() 

timeout = Timeout(30)

start = time.time()

def main():
    reader = csv.reader(file('top.csv', 'rb'))
    hosts = []
    for line in reader:
        hosts.append(line[1])
    hosts = zip(*(hosts[i::20] for i in range(20)))
    
    i = 0
    for one_hosts in hosts:
        print ">>>>>hosts in ",20*i,'~',20*(i+1)
        i = i+1
        gevent.signal(signal.SIGQUIT, gevent.shutdown)
        threads = []
        for host in one_hosts:
            threads.append(gevent.spawn(task,host))
        timeout.start_new()
        try:    
            gevent.joinall(threads) 
        except Timeout:
            pass
                    
def main2():
    reader = csv.reader(file('top.csv', 'rb'))
    hosts = []
    for line in reader:
        task(line[1]) 
                          
def task(host):
    '''get the alexa
    '''	
    #gevent.sleep(0) 
    country = alexa_api(host)
    
    if country:
        add_top_hosts(host,country)
        if country == 'CN':
            ip = host_to_ip(host)
            if ip:
                info = ip_to_city(ip)
                if info:
                    add_china_hosts(host,ip,unicode(info['city']),unicode(info['isp']))
    #get the subdomain
    #gevent.sleep(0)
    subdomains = get_subdomain(host)
    if subdomains:
        for subdomain in subdomains:
            try:
                add_subdomain(subdomain,host)
            except:
                pass
    # ......
    print host," end.....","time:",time.time()-start 

if __name__=="__main__":
    main()                				 










