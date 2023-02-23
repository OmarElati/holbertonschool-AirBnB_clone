import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""
    
    def __init__(self):
        """Initialize the BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
