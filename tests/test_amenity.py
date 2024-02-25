#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_name_attribute(self):
        amenity = Amenity(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")

if __name__ == '__main__':
    unittest.main()
