#!/usr/bin/env bash

python3 -m venv venv

# shellcheck source=./venv/bin/activate
source ./venv/bin/activate

# Install serverless plugin dependencies
yarn install

pip install --upgrade pip
pip install -r .requirements/requirements.txt