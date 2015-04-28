#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

DEV_LOG_FORMAT = '%(asctime)s %(levelname).4s:[%(name)12.12s|%(filename)-16.16s:%(lineno)4d] %(message)s'
PROD_LOG_FORMAT = '[%(name)s|%(filename)s:%(lineno)d] %(message)s'

import logging
import os
import sys


def init_logging(level=logging.INFO, prod=False):
    # Note: Logging here does not affect the dev_appserver, which logs HTTP traffic.
    # (Use --dev_appserver_log_level=warning)
    logging.getLogger().handlers[0].setFormatter(logging.Formatter(PROD_LOG_FORMAT if prod else DEV_LOG_FORMAT))
    logging.getLogger().setLevel(level)


def init_paths(root):
    # Merge the pip libraries (incl. google.protobuf) with the system path.
    # This directory contains links to required modules from ./python/lib/python2.7/site-packages
    # https://developers.google.com/appengine/articles/deferred?csw=1
    # http://stackoverflow.com/questions/2710861/how-to-import-modules-in-google-app-engine
    lib = os.path.join(root, 'lib')
    sys.path.insert(0, lib)

    # Merge lib/google with SDK.
    import google
    google.__path__.append(os.path.join(lib, 'google'))
