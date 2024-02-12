#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from models.city import City


class TestCityAttributes(unittest.TestCase):
    """Testing my Modules"""
    def test_default_attribute_values(self):
        """Test that the City class attributes have the correct default values."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_types(self):
        """Test that the City class attributes are of the correct types."""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == '__main__':
    unittest.main()
