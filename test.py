from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io
import logging

class Test(TestCase):
    @patch('builtins.input', side_effect=["61.2", "1.81"])
    def test_bmi(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            self.assertRegex(mock_stdout.getvalue(), r"The body mass index is: 18.7")
            sys.modules.pop('main')

    @patch('builtins.input', side_effect=["50.9", "1.6"])
    def test_bmi(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            self.assertRegex(mock_stdout.getvalue(), r"The body mass index is: 19.9")
            sys.modules.pop('main')

    @patch('builtins.input', side_effect=["78.8", "1.56"])
    def test_bmi(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            self.assertRegex(mock_stdout.getvalue(), r"The body mass index is: 32.4")
            sys.modules.pop('main')


if __name__ == '__main__':
    unittest.main()
