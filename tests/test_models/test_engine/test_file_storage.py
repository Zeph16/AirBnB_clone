#!/usr/bin/python3
""" Unittest for FileStorage class """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ Unittest for FileStorage class """

    my_model = BaseModel()

    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Verify save and reload functions """
        self.my_model.full_name = "An Instance"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """ Verify save, reload and update functions """
        self.my_model.my_name = "One"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "One")

        create1 = bm_dict['created_at']
        update1 = bm_dict['updated_at']

        self.my_model.my_name = "Two"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = bm_dict['created_at']
        update2 = bm_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict['my_name'], "Two")

    def testHasAttributes(self):
        """ Verify that attributes exist """
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """ Verify that JSON exists """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """ Verify reload """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """ Verify save """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def test_save_FileStorage(self):
        """ Verify new """
        var1 = self.my_model.to_dict()
        new_key = var1['__class__'] + "." + var1['id']
        storage.save()
        with open("storage.json", 'r') as fd:
            var2 = json.load(fd)
        new = var2[new_key]
        for key in new:
            self.assertEqual(var1[key], new[key])

if __name__ == '__main__':
    unittest.main()
