FROM python:3.9-slim

RUN apt update && \
    apt full-upgrade -y && \
    apt install gcc libmariadb-dev git -y

RUN mkdir /python_app

WORKDIR /python_app

COPY requirements.txt /python_app/

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ADD ./ /python_app/