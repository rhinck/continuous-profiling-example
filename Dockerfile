FROM python:3.9.5-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY Pipfile Pipfile.lock /project/

RUN pip install --upgrade pip \
    pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear

COPY . /project
