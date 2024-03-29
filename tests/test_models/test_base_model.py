#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Testing my Modules"""

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
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test converting the instance to a dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        # Check that the timestamps are in ISO format
        self.assertRegex(model_dict['created_at'],
                         r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z?$')
        self.assertRegex(model_dict['updated_at'],
                         r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z?$')

    @patch('models.storage')
    def test_save(self, mock_storage):
        # Create an instance of BaseModel
        bm = BaseModel()

        # Save the current updated_at value for later comparison
        original_updated_at = bm.updated_at

        # Call the save method
        bm.save()

        # Check that updated_at has been updated
        self.assertNotEqual(bm.updated_at, original_updated_at)
        self.assertIsInstance(bm.updated_at, datetime)

        # Check that storage.save() was called once
        mock_storage.save.assert_called_once()

    def test_str(self):
        """Testing my __str__ method"""
        bm = BaseModel()
        d = {}
        d = bm.__str__()
        self.assertIsNotNone(d)
        self.assertIsInstance(d, str)

    def test_id(self):
        """Testing my ID generation Process"""
        bm = BaseModel()
        self.assertIsNotNone(bm.id)
        self.assertIsInstance(bm.id, str)


if __name__ == '__main__':
    unittest.main()
