FROM ubuntu:latest
RUN rm -rf /var/lib/apt/lists/* && apt-get update -y

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
    

COPY ./api_server/requirements.txt ./
RUN pip3 install -U pip setuptools && pip3 --no-cache-dir install -r requirements.txt

