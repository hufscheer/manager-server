FROM python:3.9.6

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y install vim apt-utils && apt-get clean
RUN mkdir /project
ADD . /project

WORKDIR /project

RUN pip install --upgrade pip

COPY pyproject.toml poetry.lock ./

RUN chmod +x start.sh

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

EXPOSE 8000
