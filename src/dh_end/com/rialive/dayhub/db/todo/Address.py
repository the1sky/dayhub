__author__ = 'dumingtan'

from sqlobject import *

class Address(SQLObject):
    street = StringCol()
    city = StringCol()
    state = StringCol(length=2)
    zip = StringCol(length=9)
    person = ForeignKey('Person')
