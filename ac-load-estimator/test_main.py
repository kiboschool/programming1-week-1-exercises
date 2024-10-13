from unittest.mock import patch
from unittest import TestCase
import unittest
import sys

class Test(TestCase):
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["12", "15", "4"])
    def test_12x15x4(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with(18.24)
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["100", "100", "100"])
    def test_100x100x100(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with(1006.0)
        finally:
            sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
