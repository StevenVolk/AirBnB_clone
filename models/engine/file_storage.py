#!/usr/bin/python3
import json
import os
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
            FileStorage.__objects[type(obj).__class__ + "." + obj.id] = obj

    def save(self):
        r_object = self.reload()
        if r_object:
            for key, value in FileStorage.__objects:
                r_object[key] = value
        else:
            r_object = FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(r_object))

    def reload(self):
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path) as rd:
                r_file = rd.read()
            FileStorage.__objects = json.loads(r_file)
