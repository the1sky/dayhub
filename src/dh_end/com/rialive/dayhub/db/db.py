__author__ = 'dumingtan'
from com.rialive.dayhub.db.todo.Person import *
from com.rialive.dayhub.db.todo.Address import *
from com.rialive.dayhub.db.todo.User import *
from com.rialive.dayhub.db.todo.Role import *

# drop tables
Person.dropTable()
Address.dropTable()
User.dropTable()
Role.dropTable()

#create tables
Person.createTable()
Address.createTable()
User.createTable()
Role.createTable()