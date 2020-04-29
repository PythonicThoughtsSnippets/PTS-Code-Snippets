# Python Thoughts Snippet #12 - Logging library-wide, reviewed
# Python 3.7
# 2020/04/30
# post: https://pythonicthoughtssnippets.github.io/2020/04/30/PTS12-logging-library-wide-and-to-end-users_version_2.html

# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE TO RAISE DISCUSSION.

# As a common practice in my Pythonic Thoughts Snippets,
# I am not going into the details of the minor implementations,
# on doubts please search elsewhere on the web, there are countless of
# amazing explanations; here, we focus on the broader concept.

# pseudo code

# in src/sampleproject/__init__.py
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# defines the handler
_ch = logging.StreamHandler()  # creates the handler
_ch.setLevel(logging.INFO)  # sets the handler info
_ch.setFormatter(logging.Formatter(INFOFORMATTER))  # sets the handler formatting

# adds the handler to the global variable: log
log.addHandler(_ch)




# in src/sampleproject/logger.py
DEBUGFORMATTER = '%(filename)s:%(name)s:%(funcName)s:%(lineno)d: %(message)s'
"""Debug file formatter."""

INFOFORMATTER = '%(message)s'
"""Log file and stream output formatter."""



def init_log_files(log, mode='w'):
    """
    Initiate log files.

    Two files are initiated:

    1. :py:attr:`myapp.logger.DEBUGFILE`
    2. :py:attr:`myapp.logger.INFOFILE`

    Adds the two files as log Handlers to :py:attr:`log`.

    Parameters
    ----------
    mode : str, (``'w'``, ``'a'``)
        The writing mode to the log files.
        Defaults to ``'w'``, overwrites previous files.    """
    # here I show a very simple configuration
    # but you can extend it to how many handlers
    # and tweaks you need.
    db = logging.FileHandler(DEBUGFILE, mode=mode)
    db.setLevel(logging.DEBUG)
    db.setFormatter(logging.Formatter(DEBUGFORMATTER))

    info = logging.FileHandler(INFOFILE, mode=mode)
    info.setLevel(logging.INFO)
    info.setFormatter(logging.Formatter(INFOFORMATTER))

    log.addHandler(db)
    log.addHandler(info)
```

