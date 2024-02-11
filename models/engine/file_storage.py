#!/usr/bin/python3
"""My File Storage System"""
import json


class FileStorage:
    """My functions that do the saving Logic"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returning the Objects as its a private VARIABLE"""
        return FileStorage.__objects

    def new(self, obj):
        """Making A new Instance and adding it"""
        Nstring = f'{self.__class__.__name__}.{obj.id}'
        FileStorage.__objects[Nstring] = obj

    def save(self):
        """Saving Changed to My Json File"""
        Serializable = {k: v.to_dict() for k, v in
                        FileStorage.__objects.items()}
        jsonString = json.dumps(Serializable)
        with open(FileStorage.__file_path, "w") as f:
            f.write(jsonString)

    def reload(self):
        """Reloading the Data saved in my Json File
        each time the program RUNS"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    cls = globals().get(cls_name)
                    if cls and hasattr(cls, '__init__'):
                        self.new(cls(**o))
        except FileNotFoundError:
            pass
