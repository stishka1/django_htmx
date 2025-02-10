# pull the official base image
FROM python:3.11.11-alpine3.20

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY .. /usr/src/app