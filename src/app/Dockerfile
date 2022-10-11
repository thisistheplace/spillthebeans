# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim-buster

# Copy local code to the container image.
ENV APP_HOME src/app
WORKDIR $APP_HOME

# set environment variables
#   prevents python writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#   prevents python buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Install Python dependencies and Gunicorn
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir gunicorn
RUN groupadd -r app && useradd -r -g app app

# Install tkinter to satisfy ploty dependency
RUN apt-get -qq -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq -y install \
        tk-dev

# Copy the rest of the codebase into the image
COPY . ./

# Remove static files since these should be served by nginx server
# RUN rm -rf assets