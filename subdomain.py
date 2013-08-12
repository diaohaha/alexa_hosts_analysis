import string  
import urllib2  
import re
from gevent import monkey
monkey.patch_all() 

def get_subdomain(host):
    '''get the host's subdomain
    '''
    subdomains = []
    url = 'http://alexa.chinaz.com/?domain='+host
    i = 5
    while i:
        i = i-1
        try: 
            page = urllib2.urlopen(url).read()
            items = re.findall('Redirect\.asp.*?"',page,re.S)
            for item in items:
                #temp1 and temp2 is use to get the real subdomain
                temp1 = item.split("=")
                temp2 = temp1[1].split('"')
                if temp2[0] == 'OTHER':
                    pass
                else:    
                    subdomains.append(temp2[0])    
            return subdomains
        except:
			pass
    return False			    
           

if __name__=="__main__":
    subdomains = get_subdomain("uol.com.br")
    print subdomains
    
