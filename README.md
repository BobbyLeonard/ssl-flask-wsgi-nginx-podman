# ssl-flask-wsgi-nginx-podman
```podman build --tag my_wsgi .```

```podman run --name my_wsgi -p 1443:443 -d my_wsgi:latest```

Creates a Self-Signed SSL cert based on the containers hostname.
API responds to GET and and POST requests.
POST data and timestamp are written to a sqlite3 DB in the container.
