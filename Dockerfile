FROM python:3.11.2-slim-buster

WORKDIR /app

 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update 
#     && apt-get install -y --no-install-recommends \
#         gcc \
#         libpq-dev \
#         postgresql-client

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
 

COPY . .