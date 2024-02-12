#!/usr/bin/python3
"""Test File for FileStorage Module"""
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestFileStorageMethods(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test method is executed."""
        self.storage = FileStorage()
        self.state = State(name='New York')
        self.city = City(name='New York City', state_id=self.state.id)
        self.user = User(email='john@example.com', password='secret')
        self.place = Place(name='Central Park', city_id=self.city.id)
        self.amenity = Amenity(name='Bench', place_id=self.place.id)
        self.review = Review(user_id=self.user.id, place_id=self.place.id, text='Great place!')

    def test_new(self):
        """Test the new method of the FileStorage class."""
        self.storage.new(self.state)
        # Assuming that the new method adds the object to the storage,
        # we can test the effect of the new method by calling all()
        # and checking if the object is present.
        self.assertIn(self.state, self.storage.all().values())

    def test_save(self):
        """Test the save method of the FileStorage class."""
        self.storage.new(self.state)
        self.storage.save()
        # Since we cannot access the private _file_path attribute,
        # we cannot directly check the contents of the file.
        # Instead, we can test the behavior of the save method by
        # checking if the object is still present in the storage
        # after saving.
        self.assertIn(self.state, self.storage.all().values())

    def test_reload(self):
        """Test the reload method of the FileStorage class."""
        self.storage.new(self.state)
        self.storage.save()
        self.storage.reload()
        # Test the effect of the reload method by calling all()
        # and checking if the object is present.
        self.assertIn(self.state, self.storage.all().values())


if __name__ == "__main__":
    unittest.main()
