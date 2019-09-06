# Python Thoughts Snippet #3 - Setting up a library wide logging
# Python 3.7
# 2019/08/26
# post: https://pythonicthoughtssnippets.github.io/#3-logging-library-wide-and-to-end-users
# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE TO RAISE DISCUSSION.

"""
Setting up a logging system library wide and end-user driven.
"""

# As a common practice in my Pythonic Thoughts Snippets,
# I am not going into the details of the minor implementations,
# on doubts please search elsewhere on the web, there are countless of
# amazing explanations; here, we focus on the broader concept.

import os
import sys
import contextlib
from pathlib import Path
import logging
import logging.handlers

info_fmt = logging.Formatter("%(message)s")


def init_logger(name):
    
    # here we set the global logger that only print to the
    # SYS STDOUT. In this way when your libraries are covered
    # with a logging system when used by other developers.
    # yet a .log and .debug files are not created.
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # print to console
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(Logger.info_fmt)
    
    logger.addHandler(ch)
    
    self.log = logger


def set_enduser_logger(logger, path):
    """
    Sets log files when base API is used buy end users.
    """
    # the strategy on how to set up the actually logger is up to you.
    # here I should you the one I use for my projects.
    
    # I like to have info and debug files separated.
    # users can use info for their work and debug serves to communicate
    # between users and developers
    info_filename = os.fspath(Path(path, Logger.info_filename).resolve())
    debug_filename = os.fspath(Path(path, Logger.info_filename).resolve())
    
    with contextlib.suppress(FileNotFoundError):
        os.remove(debug_filename)
        os.remove(info_filename)
    
    debug_fmt = logging.Formatter(
        "%(message)s"
        "`%(levelname)s - "
        "%(filename)s:%(name)s:%(funcName)s:%(lineno)d`\n"
        )
    debughandler = logging.handlers.RotatingFileHandler(
        debug_filename,
        maxBytes=10485760,
        mode="a",
        )
    debughandler.setFormatter(debug_fmt)
    debughandler.setLevel(logging.DEBUG)
    
    debugmemhandler = logging.handlers.MemoryHandler(
        1000,
        target=debughandler,
        flushLevel=logging.ERROR,
        )
    
    debugmemhandler.setFormatter(debug_fmt)
    debugmemhandler.setLevel(logging.DEBUG)
    
    infohandler = logging.handlers.RotatingFileHandler(
        info_filename,
        maxBytes=10485760,
        mode="a",
        )
    
    infohandler.setLevel(logging.INFO)
    infohandler.setFormatter(Logger.info_fmt)
    
    infomemhandler = logging.handlers.MemoryHandler(
        1000,
        target=infohandler,
        flushLevel=logging.ERROR,
        )
    
    infomemhandler.setLevel(logging.INFO)
    infomemhandler.setFormatter(Logger.info_fmt)
    
    # add handlers
    logger.addHandler(debugmemhandler)
    logger.addHandler(infomemhandler)
    

def silence(logger):
    logger.setLevel(logging.WARNING)


def unsilence(logger):
    logger.setLevel(logging.DEBUG)

# Now, in the __init__.py of the project's base folder we will set up
# the logger singleton :) singletons in Python are simply variables in a module

# I do it this way:

import MyApp.logger as LOGGER
log = LOGGER.init_logger(__name__)

# Now from every other module MyApp.log is the log handler.
# in the base.py API (aimed to be used by end users and not by lib users)
# the .info and .debug files are setup at the API.__init__ by calling
from MyApp import log
from MyApp.logger import set_enduser_logger
class MyApp:
    def __init__(self):
        set_enduser_logger(log, self.resultsp)
        
# Likewise in the other app's libs we can use the same approach
# but without .set_enduser_logger
from MyApp import log
from MyApp.logger import silence, unsilence
class MyPackage1:
    def __init__(self):
        self.log = log  # this is optional, you can just ust log directly
        
        # you can silence the log easily:
        silence(log)
        log.info('this will be silenced')
        
        unsilence(log)
        log.info('back again')