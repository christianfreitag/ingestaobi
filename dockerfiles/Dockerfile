FROM python:3.11.6

WORKDIR /app

COPY data .
COPY dockerfiles/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ingestaobi/app/ .
