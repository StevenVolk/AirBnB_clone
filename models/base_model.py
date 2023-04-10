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
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) {}"\
                .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
