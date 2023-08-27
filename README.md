# SQLAlchemy AsyncSession + FastAPI
A blog application that creates users, posts and comments using the `SQLAlchemy`'s asyncio extension for creating sessions.
Rest API exposed with `FastAPI` and `Locust` library used for stress testing.

## Install dependencies
Execute:
```
make shell
make install
```
## Usage
Run the database migrations:
```
make migrate-generate # Optional, migrations already included in repo 
make migrate
```
Start the application
```
make run
```
Then go to http://localhost:8000/docs to see the SwaggerUI app.