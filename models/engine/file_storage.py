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
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from models.base_model import BaseModel
        import os
        from datetime import datetime

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }

        try:
            if os.path.exists(FileStorage.__file_path):
                    with open(FileStorage.__file_path, "r") as f:
                        objdict = json.load(f)
                        for key, Value in objdict.items():
                            cls_name = Value.get("__class__")
                            if cls_name and cls_name in classes:
                                del Value["__class__"]
                                cls = classes[cls_name]
                                # if "created_at" in Value:
                                #     Value["created_at"] = datetime.fromisoformat(Value["created_at"])
                                # if "updated_at" in Value:
                                #     Value["updated_at"] = datetime.fromisoformat(Value["updated_at"])
                                self.new(cls(**Value))
        except FileNotFoundError:
            pass
