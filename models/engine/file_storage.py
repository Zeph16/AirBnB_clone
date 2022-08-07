#!/usr/bin/python3
""" Serializes and Deserializes instances to and from a JSON file """
import json
import os


class FileStorage:
    """ Functions to serialize and deserialize instances """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """ Returns '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in '__objects' the obj with key '<obj class name>.id' """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """ Deserializes __objects from the JSON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        from models.city import City
        from models.place import Place
        from models.state import State
        dct = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'City': City,
            'Amenity': Amenity,
            'State': State,
            'Review': Review,
            }
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
