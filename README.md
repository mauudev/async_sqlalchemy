# SQLAlchemy AsyncSession + FastAPI
A blog application exposed with `FastAPI` that creates users, posts and comments using the `SQLAlchemy`'s asyncio extension for creating sessions.


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
