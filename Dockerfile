# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

RUN apk update \
&& apk add curl

RUN apk add libpq-dev postgresql-dev postgresql-client build-base \
&& cd /usr/local/bin \
&& pip3 install --upgrade pip

# Install python packages
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN curl -sSL https://install.python-poetry.org | python3 - \
&& export PATH="/root/.local/bin:$PATH" \
&& poetry config virtualenvs.create false \
&& poetry install --no-root

ENV PATH="${PATH}:/root/.local/bin"

COPY . /app
RUN chmod +x scripts/entrypoint.local.sh
ENTRYPOINT ["scripts/entrypoint.local.sh"]

FROM builder as dev-envs

RUN <<EOF
apk update
apk add git bash
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
