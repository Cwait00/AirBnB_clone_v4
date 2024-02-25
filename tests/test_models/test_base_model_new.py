#!/usr/bin/python3

import unittest
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModelInstantiation(unittest.TestCase):
    def test_new_instance_stored_in_objects(self):
        with patch('models.storage') as mock_storage:
            # Simulate storage behavior
            mock_storage.all.return_value = {}

            # Create a new instance
            instance = BaseModel()

            # Ensure the instance is stored in the mock storage
            self.assertIn(instance, mock_storage.all().values())

    # Other test cases...
    # Include other test cases for BaseModel instantiation here...

class TestBaseModelSave(unittest.TestCase):
    # Test cases for saving BaseModel instances...

class TestBaseModelToDict(unittest.TestCase):
    # Test cases for to_dict method of BaseModel...

if __name__ == "__main__":
    unittest.main()
