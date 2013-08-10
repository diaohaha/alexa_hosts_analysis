import string  
import urllib2  
import re

def get_subdomain(host):
    '''get the host's subdomain
    '''
    subdomains = []
    url = 'http://alexa.chinaz.com/?domain='+host
    while True:
        try: 
            page = urllib2.urlopen(url).read()
            items = re.findall('Redirect\.asp.*?"',page,re.S)
            break
        except:
			pass    
    for item in items:
        #temp1 and temp2 is use to get the real subdomain
        temp1 = item.split("=")
        temp2 = temp1[1].split('"')
        if temp2[0] == 'OTHER':
            pass
        else:    
            subdomains.append(temp2[0])    
    return subdomains       

if __name__=="__main__":
    subdomains = get_subdomain("github.com")
    print subdomains
    
