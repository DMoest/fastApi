# Dockerfile to run a FastAPI application in a containerized environment
# ----------------------------------------------------------------------------
# Author: Daniel Andersson
# Date: 2024-09-17
# Version: 0.1.0
# ----------------------------------------------------------------------------
# This Dockerfile is used to build a virtualized container for a FastAPI application with
# where poetry is used for dependency management. The Dockerfile is designed to be used with
# Python 3.11 and its divided into two stages. The first stage is the builder image, where
# the virtual environment is created and the dependencies are installed. The second stage is
# the runtime image, where the virtual environment is copied from the builder image and the
# application code is copied. The entrypoint is set to run the FastAPI application with the
# development server.
#
#
#

# --- The Builder Image ------------------------------------------------------
# Step 1 - The builder image, used to build the virtual environment
FROM python:3.11-buster as builder

# Step 2 - Set the author label
LABEL authors="daniel"

# Step 3 - Update, upgrade and install apt dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl \
    tree \
    git \
    fzf

# Step 4 - Install poetry
RUN pip install poetry==1.8.3

# Step 5 - Set the poetry environment variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Step 6 - Set the working directory
WORKDIR /app

# Step 7 - Copy the poetry files and install the dependencies
COPY pyproject.toml poetry.lock ./

# Step 8 - Add a README file to avoid poetry complaints
RUN touch README.md

# Step 9 - Install the dependencies with poetry, and remove the poetry cache
RUN if [ -z "$(ls -A /app)" ]; then echo "App directory is empty"; exit 1; fi

# Step 10 - Install the dependencies with poetry, and remove the poetry cache
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR



# --- The Runtime Image ------------------------------------------------------
# Step 11 - The runtime image, used to just run the code provided its virtual environment
FROM python:3.11-slim-buster as runtime

# Step 12 - Set the author label
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Step 13 - Copy the virtual environment from the builder image
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Step 14 - Copy the application code
COPY src ./src

# Step 15 - Set the entrypoint
ENTRYPOINT ["fastapi"]

# Step 16 - Add the command arguments
CMD ["dev", "--host", "127.1.0.0", "--port", "1337"]
