from z3c.sqlalchemy import Model
from z3c.sqlalchemy.interfaces import IModelProvider
from zope.interface import implements

from sqlalchemy.orm import mapper
from cesstex.db.pgsql.baseTypes import ()

from cesstex.db.pgsql.tables import ()


class CesstexModel(object):
    """
    A model providers provides information about the tables to be used
    and the mapper classes.
    """
    implements(IModelProvider)

    def getModel(self, metadata=None):
        """
        cesstex
        """
        model = Model()
        model.metadata = metadata

        metadata.create_all()
        return model