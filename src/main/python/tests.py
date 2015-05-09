#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

import unittest.loader


# Runnint tests
# 1. To run tests from the command line (simplest way to see output):
#    ./tools/python/bin/python src/main/python/tests.py
# 2. Create PyCharm Run configuration (set this working directory).
# 3. grunt nose

# Called by main and setup.py (on packaging)
def suite(test_path='.'):
    return unittest.loader.TestLoader().discover(test_path)


if __name__ == '__main__':
    import os
    import sys
    os.chdir(sys.path[0])

    # https://developers.google.com/appengine/docs/python/tools/localunittesting
    unittest.TextTestRunner(verbosity=2).run(suite('main'))
