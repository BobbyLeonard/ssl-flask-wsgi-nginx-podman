# ssl-flask-wsgi-nginx-podman
```podman build --tag my_wsgi .```
```podman run --name my_wsgi -p 1443:443 -d my_wsgi:latest```
