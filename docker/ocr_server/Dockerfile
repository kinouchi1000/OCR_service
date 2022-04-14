# Dockerfile
FROM ubuntu:18.04  
RUN rm -rf /var/lib/apt/lists/* && apt-get update -y
RUN apt-get install -y tesseract-ocr-eng

RUN apt-get update -y
RUN apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    language-pack-ja-base \
    language-pack-ja \
    sudo \
    rng-tools \
    vim \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

COPY ./ocr_server/requirements.txt ./
RUN pip3 install -U pip setuptools && pip --no-cache-dir install -r requirements.txt

