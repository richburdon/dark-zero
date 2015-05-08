#
# Copyright 2014 Alien Laboratories, Inc.
#

# Demo
# https://registry.hub.docker.com/u/tutum/quickstart-python/
# https://github.com/tutumcloud/quickstart-python/blob/master/app.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Alien'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
