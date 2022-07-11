[![Python Flask docker](https://github.com/adimajo/whiteapp_flask/actions/workflows/python-flask.yml/badge.svg)](https://github.com/adimajo/whiteapp_flask/actions/workflows/python-flask.yml)
[![Build Status](https://app.travis-ci.com/adimajo/whiteapp_flask.svg?token=opB6ydhp1rfhZkQiU4AY&branch=master)](https://app.travis-ci.com/adimajo/whiteapp_flask)
[![pipeline status](https://gitlab.com/adimajo/whiteapp_flask/badges/master/pipeline.svg)](https://gitlab.com/adimajo/whiteapp_flask/-/commits/master)

[![Coverage status](https://codecov.io/gh/adimajo/whiteapp_flask/branch/master/graph/badge.svg)](https://codecov.io/github/adimajo/whiteapp_flask?branch=master)
[![coverage report](https://gitlab.com/adimajo/whiteapp_flask/badges/master/coverage.svg)](https://gitlab.com/adimajo/whiteapp_flask/-/commits/master)

# WhiteApp Python Flask

The `WhiteApp` package / Flask app is a template of a simple Flask API which displays its current version.
The template ships with a Gitlab CI pipeline (which lints the code, documents it, runs tests, computes test coverage, checks on Sonarqube, builds a docker container and deploys it),
a Github Actions pipeline (which lints, documents and upload the documentation as github page, checks the package, computes tests and coverage, builds a docker container and uploads it to Github),
and a Travis pipeline (for elegant display of code coverage). 

## Sonarcloud

If you want to leverage the static code analysis (and nice display!) provided by Sonarcloud, link your Github account
to Sonarcloud at [sonarcloud.io](https://sonarcloud.io/).

## Using the Github Actions pipeline

Nothing to do! If you import your project in Sonarcloud, it will automatically trigger its analysis at each push
(see "SonarCloud Automatic Analysis" under Administration > Analysis Method).

## Using the Gitlab CI pipeline

Set the following environment variables in Gitlab's UI under Settings > CI/CD. These are not hardcoded into the pipeline
since I use the same pipeline at Crédit Agricole S.A. with our own instances of Gitlab, Gitlab runners, Sonar, etc.

`CURRENT_TAG`: the tag of an available public Gitlab runner, e.g. `docker`

`PYPI_REMOTE`: the URL to your favorite PyPi remote, e.g. `https://pypi.org/simple`

`BOOT_SONAR_INSTANCE`: `https://sonarcloud.io/`

`BOOT_SONAR_TOKEN`: you can obtain this token by logging in to [sonarcloud.io](https://sonarcloud.io/) and generating a key.

`CI_REGISTRY`: the Docker registry on which to upload the image, e.g. index.docker.io or registry.gitlab.com

`CI_REGISTRY_USER`: your registry username, e.g. Gitlab or Dockerhub username

`CI_REGISTRY_PASSWORD`: your registry password (or access token), e.g. Gitlab or Dockerhub username

## Using the Travis pipeline

Connect to [app.travis-ci.com](https://app.travis-ci.com/) and [app.codecov.io](https://app.codecov.io) to connect your repo.

The pipeline installs devtools, the dependencies of the application, documents it, checks it, computes code coverage
and sends it to [app.codecov.io](https://app.codecov.io) to display it nicely on this README.

## Installation

### Python Environnement

This project is tested againt **python 3.8 and 3.9**. It ultimately build a Docker container.

This project uses **pipenv** as a dependency manager, [see here](https://moodle.insa-rouen.fr/pluginfile.php/75430/mod_resource/content/4/Python-PipPyenv.pdf).

All dependencies are listed in `Pipfile`.
They can be installed with `pipenv install [-d] [--skip-lock]`.

To download these dependencies to install them on an offline computer,
use  `pipenv lock -r > requirements.txt` and `pip download -d TARGET_FOLDER -r requirements.txt`.

## Disclaimer

Supported by Groupe Crédit Agricole; analyses and opinions of the author(s) expressed in this work are their own.
