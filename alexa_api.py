# coding: utf-8

import urllib2
from xml.etree import ElementTree
from gevent import monkey
monkey.patch_all() 


def alexa_api(host):
    i = 5
    while i:
        i = i-1
        try:
            url = 'http://data.alexa.com/data?cli=10&dat=snbamz&url='+host
            content = urllib2.urlopen(url).read()
            root = ElementTree.fromstring(content)
            nood = root.find("SD/COUNTRY")
            #get the country code
            return nood.attrib['CODE']
        except:
			continue
    return False			      

if __name__=="__main__":
    print alexa_api('bing.com')
