#!/usr/bin/python3
""" Used to import modules and packages, and the storage object """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
