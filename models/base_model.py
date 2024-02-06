#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
class BaseModel:
    
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

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictC = vars(self)
        dictC['created_at'] = self.created_at.isoformat()
        dictC['updated_at'] = self.updated_at.isoformat()
        dictC['__class__'] = self.__class__.__name__
        return dictC
