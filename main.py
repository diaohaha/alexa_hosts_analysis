# coding: utf-8

import csv
from alexa_api import alexa_api
from host_to_ip import host_to_ip
from ip_to_city import ip_to_city
from dblib import add_top_hosts,add_subdomain,add_china_hosts
from subdomain import get_subdomain
import gevent

def main():
    reader = csv.reader(file('top.csv', 'rb'))
    hosts = []
    for line in reader:
        hosts.append(line[1])
    hosts = zip(*(hosts[i::10] for i in range(10)))
    
    for one_hosts in hosts:
        threads = []
        for host in one_hosts:
            threads.append(gevent.spawn(task,host))
        gevent.joinall(threads)  
                    
                    
def task(host):
    #host is a list type,host[1] is the real host
    print host 
    country = alexa_api(host)
    if country:
        add_top_hosts(host,country)
        if country == 'CN':
            ip = host_to_ip(host)
            if ip:
                info = ip_to_city(ip)
                if info:
                    add_china_hosts(host,ip,info['city'],str(info['dma_code']))

    #get the subdomain
    subdomains = get_subdomain(host)
    for subdomain in subdomains:
        add_subdomain(subdomain,host)
    # ......
     

if __name__=="__main__":
    main()                				 










