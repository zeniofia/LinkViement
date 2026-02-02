# test_linkviement.py
"""
Tests for LinkViement module.
"""

import unittest
from linkviement import LinkViement

class TestLinkViement(unittest.TestCase):
    """Test cases for LinkViement class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LinkViement()
        self.assertIsInstance(instance, LinkViement)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LinkViement()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
