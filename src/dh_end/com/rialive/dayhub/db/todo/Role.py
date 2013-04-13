__author__ = 'dumingtan'

from sqlobject import *

class Role(SQLObject):
    name = StringCol(alternateID=True, length=20)
    users = RelatedJoin( 'User' )
