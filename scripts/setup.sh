#!/usr/bin/env bash

python3 -m venv venv

# shellcheck source=./venv/bin/activate
source ./venv/bin/activate

# Install serverless plugin dependencies
npm i -g serverless
yarn install

echo "Creating .env file"
cp .env{.example,}

pip install --upgrade pip
pip install -r requirements.txt