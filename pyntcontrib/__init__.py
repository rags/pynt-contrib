import contextlib
import os
from subprocess import check_call, CalledProcessError
import sys
from pynt import task
__license__ = "MIT License"
__contact__ = "http://rags.github.com/pynt-contrib/"


@contextlib.contextmanager
def safe_cd(path):
    """
    Changes to a directory, yields, and changes back.
    Additionally any error will also change the directory back.

    Usage:
    >>> with safe_cd('some/repo'):
    ...     call('git status')
    """
    starting_directory = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(starting_directory)


@task()
def execute(script, *args, **kwargs):
    """
    Executes a command through the shell. Spaces should breakup the args. Usage: execute('grep', 'TODO', '*')
    NOTE: Any kwargs will be converted to args in the destination command.
    E.g. execute('grep', 'TODO', '*', **{'--before-context': 5}) will be $grep todo * --before-context=5
    """

    popen_args = [script] + list(args)
    if kwargs:
        popen_args.extend(_kwargs_to_execute_args(kwargs))

    try:
        return check_call(popen_args, shell=False)
    except CalledProcessError as ex:
        _print(ex)
        sys.exit(ex.returncode)
    except Exception as ex:
        _print('Error: {} with script: {} and args {}'.format(ex, script, args))
        sys.exit(1)


def _kwargs_to_execute_args(kwargs):
    args = ['='.join([key, value]) for key, value in kwargs.items()]
    return args


def _print(*args):
    print(args)