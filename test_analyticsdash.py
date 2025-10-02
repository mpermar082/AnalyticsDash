# test_analyticsdash.py
"""
Tests for AnalyticsDash module.
"""

import unittest
from analyticsdash import AnalyticsDash

class TestAnalyticsDash(unittest.TestCase):
    """Test cases for AnalyticsDash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnalyticsDash()
        self.assertIsInstance(instance, AnalyticsDash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnalyticsDash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
