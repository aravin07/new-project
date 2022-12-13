FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev curl

# RUN pip install --upgrade pip
# RUN pip install --upgrade setuptools==58
RUN python -m pip install --upgrade setuptools pip wheel
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
