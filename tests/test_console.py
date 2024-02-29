#!/usr/bin/python3

import unittest
from console import HBNBCommand
import io
import sys

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create(self):
        # Redirect stdout to capture console output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call create command with arguments
        self.console.onecmd("create BaseModel")

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Assert that the expected output is in the captured output
        self.assertIn("created", captured_output.getvalue())

    def test_show(self):
        # Redirect stdout to capture console output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call show command with arguments
        self.console.onecmd("show BaseModel 1234-1234-1234")

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Assert that the expected output is in the captured output
        self.assertIn("1234-1234-1234", captured_output.getvalue())

    # Add more test cases for other console commands as needed

if __name__ == "__main__":
    unittest.main()
