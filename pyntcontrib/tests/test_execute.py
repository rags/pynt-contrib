from subprocess import CalledProcessError
import unittest
import mock

from .. import execute

__version__ = "0.1.0"
__license__ = "MIT License"
__contact__ = "http://rags.github.com/pynt-contrib/"


class TestExecute(unittest.TestCase):

    @mock.patch('pyntcontrib.check_call')
    @mock.patch('pyntcontrib._print')
    @mock.patch('pyntcontrib.sys.exit')
    def test_successful_command(self, mock_exit, mock_print_, mock_check_call):
        """A successful command should not exit"""
        execute('python', '-V')

        self.assertFalse(mock_exit.called)
        self.assertFalse(mock_print_.called)
        self.assertTrue(mock_check_call.called)

    @mock.patch('pyntcontrib.check_call')
    @mock.patch('pyntcontrib._print')
    @mock.patch('pyntcontrib.sys.exit')
    def test_bad_command(self, mock_exit, mock_print_, mock_check_call):
        """A bad command should exit with the error code"""
        command = ['notatall', 'athing']
        mock_check_call.side_effect = CalledProcessError(1, command)

        execute(*command)

        self.assertTrue(mock_exit.called)
        self.assertTrue(mock_print_.called)
        self.assertTrue(mock_check_call.called)