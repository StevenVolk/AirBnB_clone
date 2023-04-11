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
            self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        r_object = {}
        for key, value in self.__objects.items():
            r_object[key] = value
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(r_object))

    def reload(self):
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as rd:
                for key, value in (json.load(rd)).items():
                    self.__objects[key] = value
