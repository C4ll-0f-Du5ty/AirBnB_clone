#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from models.state import State


class TestStateAttributes(unittest.TestCase):
    """Testing my Modules"""
    def test_default_attribute_values(self):
        """Test that the State class attributes have the correct default values."""
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_types(self):
        """Test that the State class attributes are of the correct types."""
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
