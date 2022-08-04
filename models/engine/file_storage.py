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
        dct = {'BaseModel': BaseModel}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))