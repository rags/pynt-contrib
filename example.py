#!/usr/bin/python
from pynt import task
from pyntcontrib import safe_cd, execute

#TODO: write this up
@task()
def pwd_ls(dir="/tmp"):
    '''Clean build directory.'''
    with safe_cd(dir):
        execute('pwd')
    execute("ls",dir)

__DEFAULT__ = pwd_ls
