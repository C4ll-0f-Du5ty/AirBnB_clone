#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up the test case"""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Clean up after the test case"""
        self.storage.save()

    def test_default_attribute_values(self):
        """Test that the User class attributes have the correct default values."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        """Test that the User class attributes are of the correct types."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_initialization(self):
        """Test that a User object is initialized with the correct attributes."""
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_attributes_are_private(self):
        """Test that the User object's attributes are private."""
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        
        # Attempt to access the attributes directly
        with self.assertRaises(AttributeError):
            user._User__dict__['email']
        with self.assertRaises(AttributeError):
            user._User__dict__['password']
        with self.assertRaises(AttributeError):
            user._User__dict__['first_name']
        with self.assertRaises(AttributeError):
            user._User__dict__['last_name']

    def test_instantiate_user(self):
        """Test instantiating a User"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertEqual(hasattr(user, 'email'), True)
        self.assertEqual(hasattr(user, 'password'), True)
        self.assertEqual(hasattr(user, 'first_name'), True)
        self.assertEqual(hasattr(user, 'last_name'), True)

    def test_user_to_dict(self):
        """Test user to dict method"""
        user = User()
        user.email = "test@example.com"
        user.password = "12345678"
        user.first_name = "Test"
        user.last_name = "User"
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "12345678")
        self.assertEqual(user_dict['first_name'], "Test")
        self.assertEqual(user_dict['last_name'], "User")

    def test_user_save(self):
        """Test user save method"""
        user = User()
        user.email = "test@example.com"
        user.password = "12345678"
        user.first_name = "Test"
        user.last_name = "User"
        user.save()
        self.storage.save()

    def test_user_str(self):
        """Test user string representation"""
        user = User()
        user.email = "test@example.com"
        user.password = "12345678"
        user.first_name = "Test"
        user.last_name = "User"
        user_str = str(user)
        self.assertIsInstance(user_str, str)

    # Additional tests can be added here for other functionalities


if __name__ == '__main__':
    unittest.main()
