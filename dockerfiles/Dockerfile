FROM        ec_ubuntu
MAINTAINER  ym4199@gmail.com


COPY        . /srv/deploy_ec_docker
WORKDIR     /srv/deploy_ec_docker
RUN         /root/.pyenv/versions/deploy_ec_docker/bin/pip install -r .requirements/debug.txt


EXPOSE      80 8000