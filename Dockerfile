FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /newsfeed

ADD . /newsfeed

COPY ./requirements.txt /newsfeed/requirements.txt

RUN pip install -r requirements.txt
COPY . /newsfeed