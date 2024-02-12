#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from models.amenity import Amenity


class TestAmenityAttributes(unittest.TestCase):
    """Testing my Modules"""
    def test_default_attribute_values(self):
        """Test that the Amenity class attributes have the correct default values."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_types(self):
        """Test that the Amenity class attributes are of the correct types."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
