__author__ = 'dumingtan'

from sqlobject import *

class User(SQLObject):
    class sqlmeta:
        table = 'user_table'

    username = StringCol(alternateID=True, length=20)
    roles = RelatedJoin( 'Role' )