import unittest
from unittest.mock import patch
from io import StringIO
import atm_transactions

class TestATMOperations(unittest.TestCase):
    def setUp(self):
        """Reset balance before each test."""
        atm_transactions.savings_balance = 1000.0
    
    @patch('builtins.input', side_effect=['1', '100', '4'])
    def test_deposit_valid_amount(self, mock_input):
        """Test valid deposit operation."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1100.0)
    
    @patch('builtins.input', side_effect=['2', '500', '4'])
    def test_withdraw_valid_amount(self, mock_input):
        """Test valid withdrawal operation."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 500.0)
    
    @patch('builtins.input', side_effect=['2', '2000', '4'])
    def test_withdraw_insufficient_balance(self, mock_input):
        """Test withdrawal with insufficient balance."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1000.0)
    
    @patch('builtins.input', side_effect=['1', '-50', '4'])
    def test_deposit_negative_amount(self, mock_input):
        """Test deposit with negative amount."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1000.0)
    
    @patch('builtins.input', side_effect=['2', '-50', '4'])
    def test_withdraw_negative_amount(self, mock_input):
        """Test withdrawal with negative amount."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1000.0)
    
    @patch('builtins.input', side_effect=['1', 'abc', '4'])
    def test_deposit_invalid_input(self, mock_input):
        """Test deposit with invalid input."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1000.0)
    
    @patch('builtins.input', side_effect=['5', '4'])
    def test_invalid_choice(self, mock_input):
        """Test invalid menu choice."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1000.0)
    
    @patch('builtins.input', side_effect=['3', '4'])
    def test_check_balance(self, mock_input):
        """Test balance check operation."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1000.0)
    
    @patch('builtins.input', side_effect=['1', '0', '4'])
    def test_deposit_zero_amount(self, mock_input):
        """Test deposit with zero amount."""
        with patch('sys.stdout', new=StringIO()):
            atm_transactions.atm_operations()
        self.assertEqual(atm_transactions.savings_balance, 1000.0)

if __name__ == '__main__':
    unittest.main()