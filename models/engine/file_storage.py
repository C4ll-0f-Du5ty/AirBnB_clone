#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        Nstring = f'{self.__class__.__name__}.{obj.id}'
        FileStorage.__objects[Nstring] = obj

    def save(self):
        Serializable = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        jsonString = json.dumps(Serializable)
        with open(FileStorage.__file_path, "w") as f:
            f.write(jsonString)

    def reload(self):
        # try:
        #     with open(FileStorage.__file_path) as f:
        #         data = json.load(f)
        #         # Clear the current __objects dictionary
        #         FileStorage.__objects.clear()
        #         # Deserialize each object and add it to __objects
        #         for key, value in data.items():
        #             class_name = value.pop('__class__')  # Removes '__class__' and returns 'BaseModel'
        #             cls = globals().get(class_name)  # Retrieves the BaseModel class from the global namespace
        #             if cls:
        #                 obj = cls(**value)  # Creates a new BaseModel instance with the remaining attributes
        #                 FileStorage.__objects[key] = obj  # Stores the new instance in the __objects dictionary
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    # Safely instantiate the class using globals() and hasattr()
                    cls = globals().get(cls_name)
                    if cls and hasattr(cls, '__init__'):
                        self.new(cls(**o))
        except FileNotFoundError:
            pass

