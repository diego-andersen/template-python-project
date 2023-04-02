ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Python environment
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv ${VIRTUAL_ENV}

# Python dependencies - this avoids having to rebuild them every time code changes,
# which is what happens when you put them in pyproject.toml
COPY requirements.txt requirements.txt
RUN pip install -U pip setuptools wheel \
    && pip install -r requirements.txt

# Project assets
COPY pyproject.toml pyproject.toml
COPY bin bin
COPY tests tests
COPY src src

RUN pip install -e .
