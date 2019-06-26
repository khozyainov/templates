# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import requests
import logging
import os
import json

import locale
locale.setlocale(locale.LC_ALL, '')


application = Flask(__name__)


SMARTHOME_URL = os.getenv('SMARTHOME_URL', '')


logger = logging.getLogger("smartHome-api")
logger.setLevel(logging.DEBUG)
logfile = "/var/log/app/smartHome_api.log"
if not os.path.exists(logfile):
    with open(logfile, 'w') as lf:
        lf.write("SmartHome-api logfile created.")
fh = logging.FileHandler(logfile, encoding='utf8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info("Program started")


@application.route('/', methods=['GET',])
def index():
    return jsonify('Hi')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)
    