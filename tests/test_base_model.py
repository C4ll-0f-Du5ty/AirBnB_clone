#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
import unittest

class TestBaseModel(unittest.TestCase):

    def test_create_instance(self):
        """Test creating an instance of BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_update_timestamp(self):
        """Test updating the updated_at timestamp"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test converting the instance to a dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertTrue(model_dict['created_at'].endswith('.000000'))  # Assuming no microseconds
        self.assertTrue(model_dict['updated_at'].endswith('.000000'))  # Assuming no microseconds

if __name__ == '__main__':
    unittest.main()
