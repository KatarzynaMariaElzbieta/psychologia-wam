FROM python:3.11

RUN apt-get update && apt-get install -y libpq-dev

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install  --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

EXPOSE 8000

