# test_smartcontractforge.py
"""
Tests for SmartContractForge module.
"""

import unittest
from smartcontractforge import SmartContractForge

class TestSmartContractForge(unittest.TestCase):
    """Test cases for SmartContractForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartContractForge()
        self.assertIsInstance(instance, SmartContractForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartContractForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
