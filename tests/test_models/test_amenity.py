#!/usr/bin/python3
""" Unittest for Amenity class """
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """ Unittest for Amenity class """

    a = Amenity()

    def test_class_exists(self):
        """ Verify existence """
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_user_inheritance(self):
        """ Verify inheritance from BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def testHasAttributes(self):
        """ Verify attributes' existence """
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_types(self):
        """ Verify attributes' type """
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
