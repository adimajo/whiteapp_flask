ARG DOCKER_REGISTRY

FROM ${DOCKER_REGISTRY}python:3.8-slim

ENV PIPENV_PIPFILE whiteapp/Pipfile

# copy project
COPY . whiteapp/

EXPOSE 8000

# install dependencies
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --deploy
RUN chown nobody:nogroup /whiteapp

USER nobody

ENTRYPOINT gunicorn whiteapp.wsgi:app --bind 0.0.0.0:8000
