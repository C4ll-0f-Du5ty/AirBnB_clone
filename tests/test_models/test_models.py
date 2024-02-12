#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestModels(unittest.TestCase):

    def setUp(self):
        """Set up the test case"""
        storage.reload()

    def tearDown(self):
        """Clean up after the test case"""
        storage.reload()

    def test_instantiate_state(self):
        """Test instantiating a State"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertEqual(hasattr(state, 'name'), True)

    def test_instantiate_city(self):
        """Test instantiating a City"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertEqual(hasattr(city, 'state_id'), True)
        self.assertEqual(hasattr(city, 'name'), True)

    def test_instantiate_amenity(self):
        """Test instantiating an Amenity"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertEqual(hasattr(amenity, 'name'), True)

    def test_instantiate_place(self):
        """Test instantiating a Place"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertEqual(hasattr(place, 'city_id'), True)
        self.assertEqual(hasattr(place, 'user_id'), True)
        self.assertEqual(hasattr(place, 'name'), True)
        self.assertEqual(hasattr(place, 'description'), True)
        self.assertEqual(hasattr(place, 'number_rooms'), True)
        self.assertEqual(hasattr(place, 'number_bathrooms'), True)
        self.assertEqual(hasattr(place, 'max_guest'), True)
        self.assertEqual(hasattr(place, 'price_by_night'), True)
        self.assertEqual(hasattr(place, 'latitude'), True)
        self.assertEqual(hasattr(place, 'longitude'), True)
        self.assertEqual(hasattr(place, 'amenity_ids'), True)

    def test_instantiate_review(self):
        """Test instantiating a Review"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertEqual(hasattr(review, 'place_id'), True)
        self.assertEqual(hasattr(review, 'user_id'), True)
        self.assertEqual(hasattr(review, 'text'), True)

    # Additional tests for to_dict(), save(),
    # and other methods can be added here


if __name__ == '__main__':
    unittest.main()
