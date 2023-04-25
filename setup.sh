#!/bin/bash

# create a virtual environment
python3 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt
