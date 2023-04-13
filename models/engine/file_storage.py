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
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            FileStorage.__objects["{}.{}"\
                    .format(type(obj).__name__, obj.id)] = obj.to_dict()

    def save(self):
        r_object = {}
        r_object.update(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as f:
            for key, value in r_object.items():
                r_object[key] = value
            json.dump(r_object, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as rd:
                for key, value in (json.load(rd)).items():
                    FileStorage.__objects[key] = value
