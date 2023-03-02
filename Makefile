# Makefile
## the Makefile includes instructions on environment setup and linting
## create and activate a virtual environment
## Install dependencies in requirements.txt

setup:
	# create python virtualenv & source it
	# source ~/.nl-lambda/bin/activate
	python3 -m venv ~/.nl-lambda

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv test_cli-tanslate.py

lint:
	pylint --disable=R,C src/cli-translate.py src/translate.py

all: install test lint