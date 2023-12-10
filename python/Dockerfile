#NOTE name need to be Dockerfile
FROM python:3.9 AS builder


WORKDIR /app
ARG PIP_VERSION=23.3.1
COPY requirements.txt .
RUN pip3 install --upgrade pip==${PIP_VERSION}
RUN pip3 install -r requirements.txt

FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9//site-packages
COPY --from=builder /app .
ARG PIP_VERSION==${PIP_VERSION}
COPY . .
#----------------------------
