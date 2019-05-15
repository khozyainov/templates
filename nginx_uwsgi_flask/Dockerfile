# Use an official Python runtime as a parent image
FROM ubuntu:16.04
# Install base packages
RUN apt-get update && apt-get install -y \
  # software-properties-common \
  git \
  gcc \
  curl \
  nano \
  cron \
  nginx \
  python3.5 \
  libpython3.5 \
  python3.5-dev \
  python3.5-venv \
  python3-setuptools \
  python3-pip \
  locales \
  libpcre3 \
  libpcre3-dev \
  uwsgi \
  uwsgi-plugin-python3 \
  python-wheel \
  libssl-dev \
  supervisor && \
  apt-get update && apt-get upgrade -y && locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales && echo "daemon off;" >> /etc/nginx/nginx.conf

ADD requirements.txt /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir -r requirements.txt

ENV LC_ALL=ru_RU.UTF-8
ENV LANG=ru_RU.UTF-8
CMD ["/usr/bin/supervisord"]
