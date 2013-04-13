__author__ = 'dumingtan'

from com.rialive.dayhub.db.conn import *

class Person(SQLObject):
    firstName = StringCol()
    middleInitial = StringCol(length=1, default=None)
    lastName = StringCol()