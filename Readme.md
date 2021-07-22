# Employee service

## Running migrations

Running new migration

```bash
docker-compose run business-api alembic revision --autogenerate -m "Migration name"
```

Undo last migration

```bash
docker-compose run business-api alembic downgrade -1
```

Updating migrations

```bash
docker-compose run business-api alembic upgrade head
```
