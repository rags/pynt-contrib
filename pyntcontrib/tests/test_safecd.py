import os
import tempfile
import unittest

from pyntcontrib import safe_cd

__version__ = "0.1.0"
__license__ = "MIT License"
__contact__ = "http://rags.github.com/pynt-contrib/"


class TestSafeCd(unittest.TestCase):

    def setUp(self):
        self.cwd = os.getcwd()
        self.temp_dir = tempfile.mkdtemp('pyntcontrib')

    def test_change_yield_revert(self):
        """Safe cd should change directory, yield and revert back"""
        with safe_cd(self.temp_dir):
            os.path.exists(self.temp_dir)

        self.assertEqual(os.getcwd(), self.cwd, "Working directory was not restored.")

    def test_change_error_revert(self):
        """Should restore directory after an exception during yield"""
        try:
            with safe_cd(self.temp_dir):
                raise ValueError
        except ValueError:
            pass

        self.assertEqual(os.getcwd(), self.cwd, "Working directory was not restored.")