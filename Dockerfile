# Dockerfile
FROM python:3.6.1-alpine

WORKDIR /code
ADD . /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
