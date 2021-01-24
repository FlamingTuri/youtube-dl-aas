#!/bin/bash

source server/venv/bin/activate
export FLASK_APP=server/src/main.py
python3 -m flask run
