#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if partition[0] == cls.__name__:
                    dic[key] = self.__objects[key]
            return dic
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                json_data = json.load(file)
                for key, obj_dict in json_data.items():
                    class_name = obj_dict.get('__class__')
                    if class_name:
                        obj_class = globals().get(class_name)
                        if obj_class:
                            obj_instance = obj_class(**obj_dict)
                            self.__objects[key] = obj_instance
                        else:
                            print(f"Warning: Unknown class '{class_name}' encountered.")
                    else:
                        print(f"Warning: '__class__' key missing for object with key '{key}'.")
        except FileNotFoundError:
            print("File not found. Unable to reload data.")

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
