from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.address import router
from app.core.config import settings
from app.core.exceptions import AppException
from sqlalchemy.exc import SQLAlchemyError
from app.core.exception_handler import (
    app_exception_handler,
    db_exception_handler,
    generic_exception_handler
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API", debug=settings.DEBUG)

app.include_router(router, prefix=settings.API_V1_PREFIX + "/addresses", tags=["Addresses"])

# Register exception handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(SQLAlchemyError, db_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)