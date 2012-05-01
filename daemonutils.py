#encoding: utf-8
"""
Author: Aurélien Gâteau
License: GPLv3+
"""
import logging
import os
import sys

def double_fork():
    # Python unix daemon trick from the Activestate recipe 66012
    try:
        pid = os.fork()
        if pid > 0:
            # exit first parent
            sys.exit(0)
    except OSError, e:
        logging.error("fork #1 failed: %d (%s)", e.errno, e.strerror)
        sys.exit(1)

    # decouple from parent environment
    os.chdir("/")   #don't prevent unmounting
    os.setsid()
    os.umask(0)

    # do second fork
    try:
        pid = os.fork()
        if pid > 0:
            # exit from second parent
            sys.stdout.flush()
            sys.exit(0)
    except OSError, e:
        logging.error("fork #2 failed: %d (%s)", e.errno, e.strerror)
        sys.exit(1)
