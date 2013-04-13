from sqlobject import *
import sys, os

conn_str = 'mysql://root:nant5460300@127.0.0.1:3306/sqlobject'
conn = connectionForURI( conn_str )
sqlhub.processConnection = conn


