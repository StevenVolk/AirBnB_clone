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
        return self.__objects

    def new(self, obj):
        if obj:
            self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        r_object = self.reload()
        if r_object:
            for key, value in self.__objects:
                r_object[key] = value
        else:
            r_object = self.__objects
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(r_object))

    def reload(self):
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path) as rd:
                r_file = rd.read()
            self.__objects = json.loads(r_file)
