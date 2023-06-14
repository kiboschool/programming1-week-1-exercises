from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io
import logging

from gradescope_utils.autograder_utils.decorators import weight


class Test(TestCase):
    @patch('builtins.input', side_effect=["61.2", "1.81"])
    @weight(1)
    def test_bmi1(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            try:
                self.assertRegex(mock_stdout.getvalue(), r"The body mass index is: 18.7")
            finally:
                sys.modules.pop('main')

    @patch('builtins.input', side_effect=["50.9", "1.6"])
    @weight(1)
    def test_bmi2(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            try:
                self.assertRegex(mock_stdout.getvalue(), r"The body mass index is: 19.9")
            finally:
                sys.modules.pop('main')

    @patch('builtins.input', side_effect=["78.8", "1.56"])
    @weight(1)
    def test_bmi3(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            try:
                self.assertRegex(mock_stdout.getvalue(), r"The body mass index is: 32.4")
            finally:
                sys.modules.pop('main')


if __name__ == '__main__':
    unittest.main()
