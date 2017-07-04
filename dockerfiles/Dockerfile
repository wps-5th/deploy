FROM        ec_ubuntu
MAINTAINER  ym4199@gmail.com


COPY        . /srv/deploy_ec_docker
WORKDIR     /srv/deploy_ec_docker
RUN         /root/.pyenv/versions/deploy_ec_docker/bin/pip install -r .requirements/debug.txt

COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/

COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

CMD         supervisord -n


EXPOSE      80 8000