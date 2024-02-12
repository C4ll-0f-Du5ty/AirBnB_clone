#!/usr/bin/python3
"""My Base (Core) Module"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The Class At Which i do the operations on my Dict."""
    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returning the String Representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saving My Modification dates"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Creating A Dict. out of my Data to be Stored"""
        dictC = {}
        dictC.update(self.__dict__)
        dictC['created_at'] = self.created_at.isoformat()
        dictC['updated_at'] = self.updated_at.isoformat()
        dictC['__class__'] = self.__class__.__name__
        return dictC
