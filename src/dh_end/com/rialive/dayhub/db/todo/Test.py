__author__ = 'dumingtan'

from sqlobject import *
from conn import *

from src.dh_end.com.rialive.dayhub.db.todo.User import *
from src.dh_end.com.rialive.dayhub.db.todo.Person import *
from src.dh_end.com.rialive.dayhub.db.todo.Address import *

#add data for Person
Person( firstName='chris', lastName='du')
p = Person(firstName='bob', lastName='hope')

#create relation between Person and Address
Person.sqlmeta.addJoin( MultipleJoin( 'Address', joinMethodName='addresses'))

#add data for Address
Address( street='123 w Main St', city='beijing', state='Beijing', zip='100085', person=p )

# add data for User
#bob = User(username='bob')
#tim = User(username='tim')
#jay = User(username='jay')

#add data for Role
#admin = Role(name='admin')
#editor = Role(name='editor')

#related join
#bob.addRole(admin)
#bob.addRole(editor)
#tim.addRole(editor)

user = User.byUsername('bob')
print user

print Person.sqlmeta.expired

