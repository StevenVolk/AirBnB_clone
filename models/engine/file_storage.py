#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
"""

class FileStorage

"""


class FileStorage:
    """

    class FileStorage

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            self.__objects["{}.{}"\
                    .format(type(obj).__name__, obj.id)] = obj

    def save(self):
        r_object = {}
        r_object.update(self.__objects)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for key, value in r_object.items():
                r_object[key] = value.to_dict()
            json.dump(r_object, f)
            

    def reload(self):
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as rd:
                file_json = json.load(rd)
                for key, value in file_json.items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
