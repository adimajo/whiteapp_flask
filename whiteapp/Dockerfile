ARG DOCKER_REGISTRY
ARG PYPI_REMOTE

FROM ${DOCKER_REGISTRY}python:3.8-slim

ENV PYPI_REMOTE $PYPI_REMOTE

# copy project
COPY . whiteapp/

EXPOSE 8000

# install dependencies
RUN pip install --upgrade pip && pip install pipenv
RUN echo $PYPI_REMOTE
RUN PYPI_REMOTE=$PYPI_REMOTE PIPENV_PIPFILE=whiteapp/Pipfile pipenv install --system --deploy
RUN chown nobody:nogroup /whiteapp

USER nobody

ENTRYPOINT gunicorn whiteapp.wsgi:app --bind 0.0.0.0:8000
