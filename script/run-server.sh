#!/bin/bash

cd server
source venv/bin/activate
export FLASK_APP=src/main.py
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0
