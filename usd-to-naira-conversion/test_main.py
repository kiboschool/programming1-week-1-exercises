from unittest.mock import patch
from unittest import TestCase
import unittest
import sys

from gradescope_utils.autograder_utils.decorators import weight

class Test(TestCase):
    @patch('builtins.print')
    @patch('builtins.input', return_value="1")
    @weight(0.5)
    def test_1_USD(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("1.00 USD is 424.55 NGN")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', return_value="50")
    @weight(1)
    def test_50_USD(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("50.00 USD is 21227.50 NGN")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', return_value="14.01")
    @weight(1)
    def test_14_01_USD(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("14.01 USD is 5947.95 NGN")
        finally:
            sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
