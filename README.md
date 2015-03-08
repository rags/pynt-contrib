[![Build Status](https://travis-ci.org/rags/pynt-contrib.png?branch=master)](https://travis-ci.org/rags/pynt-contrib)

A collection of common pynt tasks
=================================

[Raghunandan Rao](https://github.com/rags)
## Installation

You can install pynt-contrib from the Python Package Index (PyPI) using pip (``pip install pynt-contrib``) or easy_install (``easy_install pynt-contrib``), or from source (``python setup.py install``)

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

**Using pynt contrib**
-----------------------

Listing the tasks in build.py

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
Note that execute is included as a task in the build scripts as a task automatically when its imported from pynt-contrib. So you can use it as any other task
```bash
$ pynt "execute[ls,-la]"
[ build.pyc - Starting task "execute" ]
total 16
drwxr-xr-x  4 raghunr  wheel  136 Mar  8 22:15 .
drwxrwxrwt  9 root     wheel  306 Mar  8 22:56 ..
-rwxr-xr-x  1 raghunr  wheel  258 Mar  8 22:14 build.py
-rw-r--r--  1 raghunr  wheel  479 Mar  8 22:15 build.pyc
[ build.pyc - Completed task "execute" ]
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
