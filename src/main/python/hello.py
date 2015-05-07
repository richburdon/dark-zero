#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

# https://github.com/tutumcloud/quickstart-python/blob/master/app.py

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
