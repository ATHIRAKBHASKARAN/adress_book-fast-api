from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from app.core.exceptions import AppException
from app.core.logging import get_logger

logger = get_logger(__name__)


async def app_exception_handler(request: Request, exc: AppException):
    logger.error(f"AppException: {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


async def db_exception_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"Database Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Database error occurred"}
    )


async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )