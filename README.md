[![Build Status](https://travis-ci.org/rags/pynt-contrib.png?branch=master)](https://travis-ci.org/rags/pynt-contrib)

A collection of common pynt tasks
=================================

[Raghunandan Rao](https://github.com/rags)
## Installation


You can install pynt from the Python Package Index (PyPI) or from source.

Using pip

```bash
$ pip install pynt-contrib
```

Using easy_install

```bash
$ easy_install pynt-contrib
```

## Example

**build.py**
------------

```python
#!/usr/bin/python
from pynt import task
from pyntcontrib import safe_cd, execute

#TODO: write this up
@task()
def pwd_ls(dir="/tmp"):
    '''Run "pwd followed by "ls" on a given directory'''
    with safe_cd(dir):
        execute('pwd')
    execute("ls",dir)

__DEFAULT__ = pwd_ls
```

**Running pynt tasks**
-----------------------

The command line interface and help is automatically generated. Task descriptions
are extracted from function docstrings.

```bash
$ pynt -l
Tasks in build file build.py:
  execute                Executes a command through the shell. Spaces should breakup the args. Usage: execute('grep', 'TODO', '*')
  pwd_ls      [Default]  Run "pwd followed by "ls" on a given directory

Powered by pynt 0.8.1 - A Lightweight Python Build Tool.
```

```bash
$ pynt "pwd_ls[/tmp/foo]"
[ build.pyc - Starting task "pwd_ls" ]
/tmp/foo
build.py	build.pyc
[ build.pyc - Completed task "pwd_ls" ]
```

pynt-contrib currently has
* execute: A ``task`` to execute os commands
* safe_cd: An utility function to safely change the context to a given directory

## Contributors/Contributing


* Ivan Ven Osdel


If you want to make changes the repo is at https://github.com/rags/pynt-contrib. You will need [pytest](http://www.pytest.org) and mock to run the tests

```bash
$ pynt
```

It will be great if you can raise a [pull request](https://help.github.com/articles/using-pull-requests) once you are done.

*If you find any bugs or need new features please raise a ticket in the [issues section](https://github.com/rags/pynt-contrib/issues) of the github repo.*
    
## License

pynt-contrib is licensed under a [MIT license](http://opensource.org/licenses/MIT)
