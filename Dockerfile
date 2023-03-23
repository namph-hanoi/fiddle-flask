FROM --platform=$BUILDPLATFORM python:3.10 AS builder
WORKDIR /app

# RUN apt-get install -y libpq-dev \
# && apt-get install -y postgresql-common \
# && apt-get install -y postgresql-client

RUN pip install --no-cache-dir pipenv
COPY Pipfile .

# Generate the Pipfile.lock during the image build process, then immediately remove the venv.
RUN pipenv lock && pipenv --clear && pipenv --rm

RUN pipenv install --system --deploy --ignore-pipfile
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]