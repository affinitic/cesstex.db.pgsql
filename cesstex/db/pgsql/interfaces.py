from zope.component.interfaces import IObjectEvent
from zope.component.interfaces import ObjectEvent
from zope.interface import implements

class IDBModelInitializeEvent(IObjectEvent):
    """
    The DB model is initialized
    """

class DBModelInitializeEvent(ObjectEvent):
    implements(IDBModelInitializeEvent)

