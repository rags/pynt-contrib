from subprocess import CalledProcessError
import unittest
import mock

from .. import execute

__version__ = "0.1.0"
__license__ = "MIT License"
__contact__ = "http://rags.github.com/pynt-contrib/"


class TestExecute(unittest.TestCase):

    def _assert_successful_call(self, mock_exit, mock_print_, mock_check_call):
        self.assertFalse(mock_exit.called)
        self.assertFalse(mock_print_.called)
        self.assertTrue(mock_check_call.called)
        self.assertDictEqual({'shell': False}, mock_check_call.call_args[1])

    @mock.patch('pyntcontrib.check_call')
    @mock.patch('pyntcontrib._print')
    @mock.patch('pyntcontrib.sys.exit')
    def test_successful_command(self, mock_exit, mock_print_, mock_check_call):
        """A successful command should not exit"""
        execute('python', '-V')

        self._assert_successful_call(mock_exit, mock_print_, mock_check_call)

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

    @mock.patch('pyntcontrib.check_call')
    @mock.patch('pyntcontrib._print')
    @mock.patch('pyntcontrib.sys.exit')
    def test_command_with_kwargs(self, mock_exit, mock_print_, mock_check_call):
        """
        Execute should convert any kwargs to args for the underlying call.

        Typical use case example:
        pynt grep_tmp[needle, --before-context=5,--after-context=3]

        @task()
        def grep_tmp(text, **options):
            args = ('grep', '-r', text, '/tmp',)
            execute(*args, **options)

        Should execute:
        grep -r needle /tmp --before-context=5 --after-context=3
        """

        args = ['grep','-r', 'needle', '/tmp']
        kwargs = {
            '--before-context': '5',
            '--after-context': '3',
        }
        execute(*args, **kwargs)

        self._assert_successful_call(mock_exit, mock_print_, mock_check_call)
        actual_call_args = [arg for arg in mock_check_call.call_args[0][0]]
        self.assertListEqual(actual_call_args[:-2], args)
        # No guaranteed order so lets just check for the converted ones
        self.assertIn('--before-context=5', actual_call_args[-2:])
        self.assertIn('--after-context=3', actual_call_args[-2:])

