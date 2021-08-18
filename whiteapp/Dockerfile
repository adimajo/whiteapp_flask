# pull official base image
FROM docker-remote.registry.saas.cagip.group.gca/library/python:3.8-slim

# copy project
COPY . .

EXPOSE 8000

# install dependencies
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install
CMD pipenv run gunicorn wsgi:app --bind 0.0.0.0:8000
