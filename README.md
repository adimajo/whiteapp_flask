[![Python Flask docker](https://github.com/adimajo/whiteapp_flask/actions/workflows/python-flask.yml/badge.svg)](https://github.com/adimajo/whiteapp_flask/actions/workflows/python-flask.yml)
[![Build Status](https://app.travis-ci.com/adimajo/whiteapp_flask.svg?token=opB6ydhp1rfhZkQiU4AY&branch=master)](https://app.travis-ci.com/adimajo/whiteapp_flask)[![Coverage status](https://codecov.io/gh/adimajo/whiteapp_flask/branch/master/graph/badge.svg)](https://codecov.io/github/adimajo/whiteapp_flask?branch=master)

# WhiteApp Python Flask

The `WhiteApp` package / Flask app is a template of a simple Flask API which displays its current version.
The template ships with a Gitlab CI pipeline (which lints the code, documents it, runs tests, computes test coverage, checks on Sonarqube, builds a docker container and deploys it),
a Github Actions pipeline (which lints, documents and upload the documentation as github page, checks the package, computes tests and coverage, builds a docker container and uploads it to Github),
and a Travis pipeline (for elegant display of code coverage). 

## Using the Github Actions pipeline

Nothing to do!

## Using the Gitlab CI pipeline

To make use of Sonar's open source facilities,
set the following environment variables in Gitlab's UI under Settings > CI/CD.

### Variables

`BOOT_SONAR_TOKEN`

You can obtain this token by logging in to [sonarcloud.io](https://sonarcloud.io/) and generating a key.

## Using the Travis pipeline

Connect to [app.travis-ci.com](https://app.travis-ci.com/) and [app.codecov.io](https://app.codecov.io) to connect your repo.

The pipeline installs devtools, the dependencies of the application, documents it, checks it, computes code coverage
and sends it to [app.codecov.io](https://app.codecov.io) to display it nicely on this README.

## Installation

### Python Environnement

This project uses **python 3.8** in a Docker container.

This project uses **pipenv** as a dependency manager, [see here](https://moodle.insa-rouen.fr/pluginfile.php/75430/mod_resource/content/4/Python-PipPyenv.pdf).

All dependencies are listed in `Pipfile`.
They can be installed with `pipenv install [-d]`.

To download these dependencies to install them on an offline computer,
use  `pipenv lock -r > requirements.txt` and `pip download -d TARGET_FOLDER -r requirements.txt`.
