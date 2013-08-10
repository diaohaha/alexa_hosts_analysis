# coding: utf-8

import urllib2
from xml.etree import ElementTree


def alexa_api(host):
    while True:
        try:
            url = 'http://data.alexa.com/data?cli=10&dat=snbamz&url='+host
            content = urllib2.urlopen(url).read()
            break
        except:
			continue    


    root = ElementTree.fromstring(content)
    nood = root.find("SD/COUNTRY")
    #get the country code
    return nood.attrib['CODE']   

if __name__=="__main__":
    print alexa_api('baidu.com')
