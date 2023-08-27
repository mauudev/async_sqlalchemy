from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from async_sqlalchemy.modules.shared import exceptions


class ApiError(BaseModel):
    detail: str


def unknown_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ApiError(detail=str(exc)).model_dump_json(),
    )


def user_exception(request: Request, exc: exceptions.UserError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ApiError(detail=str(exc)).model_dump_json(),
    )


def validation_error(request: Request, exc: exceptions.ValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ApiError(detail=str(exc)).model_dump_json(),
    )


def add_error_handler(app: FastAPI) -> FastAPI:
    app.add_exception_handler(exceptions.UserError, user_exception)
    app.add_exception_handler(exceptions.ValidationError, validation_error)
    app.add_exception_handler(Exception, unknown_exception)
    return app
