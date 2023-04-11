#!/usr/bin/env python3
import models
import uuid
from datetime import datetime
"""

class BaseModel that defines all common attributes/methods for other classes

"""


class BaseModel:
    """

    class BaseModel that defines all common attributes
    /methods for other classes

    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "created_at" in kwargs and "updated_at" not in kwargs:
                self.updated_at = self.created_at
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}"\
                .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        d_dict = dict(self.__dict__)
        d_dict["created_at"] = self.created_at.isoformat()
        d_dict["updated_at"] = self.updated_at.isoformat()
        d_dict["__class__"] = self.__class__.__name__
        return d_dict
