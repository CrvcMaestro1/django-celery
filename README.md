# Django app with celery + redis and flower

## Run
```bash
docker-compose up -d --build
```

## Run with some (ex. 3) workers
```bash
docker-compose up -d --build --scale celery=3
```

## Run tests
```bash
docker-compose exec web python -m pytest
```