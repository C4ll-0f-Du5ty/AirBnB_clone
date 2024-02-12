#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from models.place import Place


class TestPlaceAttributes(unittest.TestCase):
    """Testing my Modules"""
    def test_default_attribute_values(self):
        """Test that the Place class attributes have the correct default values."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms,  0)
        self.assertEqual(place.number_bathrooms,  0)
        self.assertEqual(place.max_guest,  0)
        self.assertEqual(place.price_by_night,  0)  # Expecting int
        self.assertEqual(place.latitude,  0.0)
        self.assertEqual(place.longitude,  0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attribute_types(self):
        """Test that the Place class attributes are of the correct types."""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)  # Expecting int
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
