FROM python:3

RUN apt update
RUN apt install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor
        
COPY nginx.conf /etc/nginx/
COPY default /etc/nginx/conf.d/
COPY snippets /etc/nginx/snippets/
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
RUN openssl req -x509 -subj $(printf '/CN=nginx_%s' "$(hostname)") -nodes -newkey rsa:4096 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -sha256 -days 365

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN useradd --no-create-home nginx

COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/supervisor/

COPY wsgi.py wsgi.py
COPY app.py app.py  

CMD ["/usr/bin/supervisord"]
