#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.state import State


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

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
