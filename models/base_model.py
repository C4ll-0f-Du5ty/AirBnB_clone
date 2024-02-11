#!/usr/bin/python3
"""My Base (Core) Module"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The Class At Which i do the operations on my Dict."""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            import models
            models.storage.new(self)

    def __str__(self):
        """Returning the String Representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saving My Modification dates"""
        self.updated_at = datetime.now()
        import models
        models.storage.save()

    def to_dict(self):
        """Creating A Dict. out of my Data to be Stored"""
        dictC = vars(self)
        if isinstance(self.created_at, datetime):
            dictC['created_at'] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            dictC['updated_at'] = self.updated_at.isoformat()
        dictC['__class__'] = self.__class__.__name__
        return dictC
