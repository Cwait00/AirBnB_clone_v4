#!/usr/bin/python3

import unittest
from models.engine.db_storage import DBStorage
from models.state import State


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.storage = DBStorage()

    def test_get(self):
        # Add test cases for get method
        state = State(name="Test State")
        self.storage.new(state)
        self.assertEqual(self.storage.get(State, state.id), state)

    def test_count(self):
        # Add test cases for count method
        self.assertEqual(self.storage.count(), 0)
        state = State(name="Test State")
        self.storage.new(state)
        self.assertEqual(self.storage.count(State), 1)


if __name__ == '__main__':
    unittest.main()
