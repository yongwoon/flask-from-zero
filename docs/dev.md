# Set Dev env

## set docker

- build image

```bash
docker-compose build --no-cache
```

- run docker

```bash
docker-compose up
```

- install package in container

```bash
pip install --upgrade -r requirements.txt
```

- Set database

```bash
python manage.py init_db
```
