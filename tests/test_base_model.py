#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_id_generation(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

if __name__ == '__main__':
    unittest.main()
