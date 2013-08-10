#! /usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import *
from sqlalchemy.orm import *
import string
import sys

class top_hosts(object):
    def _init_(self,host,country):
        self.country=country
        self.host=host

class subdomain(object):
    def _init_(self,host,father_host):
        self.host=host
        self.father_host=father_host
        
class china_hosts(object):
    def _init_(self,host,ip,city,operator):
        self.host=host
        self.ip=ip
        self.city=city
        self.operator=operator        

engine = create_engine('sqlite:///hosts.db')
metadata=MetaData(engine)


top_hosts_table=Table(
    'top_hosts',metadata,
    Column('host',String,primary_key=True),
    Column('country',String),
    )
    
subdomain_table=Table(
    'subdomain',metadata,
    Column('host',String,primary_key=True),
    Column('father_host',String),
    )
   
china_hosts_table=Table(
    'china_hosts',metadata,
    Column('host',String,primary_key=True),
    Column('ip',String),
    Column('city',String),
    Column('operator',String)
    )        
		
metadata.create_all(engine)
mapper(top_hosts,top_hosts_table)
mapper(subdomain,subdomain_table)
mapper(china_hosts,china_hosts_table)	

session=sessionmaker(bind=engine)
session=create_session()

	

def add_top_hosts(host,country):
    temp=top_hosts()
    temp.host = host
    temp.country = country
    session.add(temp)
    session.flush()
def add_subdomain(host,father_host):
    temp=subdomain()
    temp.host = host
    temp.father_host = father_host
    session.add(temp)
    session.flush()
def add_china_hosts(host,ip,city,operator):
    temp=china_hosts()
    temp.host = host
    temp.ip = ip
    temp.city = city
    temp.operator = operator
    session.add(temp)
    session.flush()        		

if __name__=="__main__":
    pass		
