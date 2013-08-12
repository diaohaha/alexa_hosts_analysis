# coding: utf-8

import pygeoip
import re
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from gevent import monkey
monkey.patch_all() 

def test_ip_format(ip):
    '''test the ip format
    '''
    ipRex = '^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$'
    tmp = re.findall(re.compile(ipRex),ip)
    if not tmp:
        return False  
    return True	
    
    
def ip_to_city(ip):
    '''get the real addr use ip, if failed return None
    '''
    record = {}
    try:
        url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip='+ip
        page=urllib.urlopen(url).read()
        data=json.loads(page)
        record['city'] = data ['city']
        record['isp'] = data['isp']
        return record
    except:
        return False



if __name__=="__main__" :
    ip = '202.108.22.5'
    if test_ip_format(ip):
        print ip_to_city(ip)['city']
        print ip_to_city(ip)['isp']
    else:
		print "format error of ip"    	
