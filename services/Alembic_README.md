# Migration steps

**NOTED** : If the non-alembic ```database.db``` exist, then deletes that file before making initial migration.

## 1. Make migrations (In each services if needed).

- Make migration according to latest model update.

```
alembic revision --autogenerate -m "migration message"
```
**NOTED** : do this step first if the file is not up to date. 
## 2. migrate the data

```
alembic upgrade head
```