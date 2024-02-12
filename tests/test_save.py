#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelSaveMethod(unittest.TestCase):
    """Testing my Save Method"""
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


if __name__ == '__main__':
    unittest.main()
