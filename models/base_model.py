#!/usr/bin/env python3
from datetime import datetime
import uuid
"""

class BaseModel that defines all common attributes/methods for other classes

"""


class BaseModel:
    """

    class BaseModel that defines all common attributes
    /methods for other classes

    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}"\
                .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
