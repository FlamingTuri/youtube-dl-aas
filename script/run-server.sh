#!/bin/bash

source server/venv/bin/activate
export FLASK_APP=server/src/main.py
python3 -m flask run --host=0.0.0.0
