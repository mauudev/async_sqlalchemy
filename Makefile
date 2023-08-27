shell:
	poetry shell;

install:
	poetry install;

run:
	poetry run python async_sqlalchemy/api/main.py

test:
	poetry run pytest tests

migrate-generate:
	poetry run alembic revision --autogenerate -m "make auto generate commit"

migrate:
	poetry run alembic upgrade head


.PHONY: shell install run test build migrate-generate migrate
