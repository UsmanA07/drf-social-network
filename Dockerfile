FROM python:3.13.1-slim

ENV POETRY_VERSION=2.0.1
RUN pip install "poetry==$POETRY_VERSION"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app/
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]