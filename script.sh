#! /bin/bash

pipenv shell
flake8 wxbot/
pylint wxbot/
