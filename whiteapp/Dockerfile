# pull official base image
FROM docker-remote.registry.saas.cagip.group.gca/library/python:3.8-slim

# copy project
COPY . whiteapp/

EXPOSE 8000

# install dependencies
RUN pip install --upgrade pip && pip install pipenv
RUN PIPENV_PIPFILE=whiteapp/Pipfile pipenv install --system --deploy
RUN chown nobody:nogroup /whiteapp

USER nobody

ENTRYPOINT gunicorn whiteapp.wsgi:app --bind 0.0.0.0:8000
