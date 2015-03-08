#!/usr/bin/python

import subprocess
from pynt import task
import os

@task()
def apidoc():
    """
    Generate API documentation using epydoc.
    """
    subprocess.call(["epydoc","--config","epydoc.config"])
    
@task()
def test(*args):
    """
    Run unit tests.
    """
    subprocess.call(["py.test-2.7"] + list(args))
    subprocess.call(["py.test-3.4"] + list(args))

@task()
def generate_rst():
    
    subprocess.call(['pandoc', '-f', 'markdown', '-t', 'rst', '-o', 'README.rst', 'README.md'])

@task(generate_rst)
def upload():
    env=os.environ.copy()
    print(env)
    env['PYTHONPATH']= "./pynt"
    print(env)
    #    subprocess.call(['ssh-add', '~/.ssh/id_rsa'])
    pipe=subprocess.Popen(['python', 'setup.py', 'sdist','upload'], env=env)
    pipe.wait()

__DEFAULT__ = test