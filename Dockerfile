FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt && \
    pip3 install -U mypy && \
    pip3 install django-stubs 
COPY . /app/