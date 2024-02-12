#!/usr/bin/python3
""" A Module To Test my Project"""
import unittest
from models.review import Review


class TestReviewAttributes(unittest.TestCase):
    """Testing my Modules"""
    def test_default_attribute_values(self):
        """Test that the Review class attributes have the correct default values."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_types(self):
        """Test that the Review class attributes are of the correct types."""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
