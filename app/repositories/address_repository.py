from sqlalchemy.orm import Session
from app.core.exceptions import AppException
from app.core.logging import get_logger
from app.models.address import Address
from sqlalchemy.exc import SQLAlchemyError
logger = get_logger(__name__)

def create(db: Session, address):
    try:
        db_address = Address(**address.dict())
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        logger.info("Address created successfully")
        return db_address
    except SQLAlchemyError:
        db.rollback()
        logger.exception("Database error while creating address")

        raise AppException("Database error occurred", 500)

    except Exception as e:
        db.rollback()
        logger.exception(f"Unexpected error: {e}")

        raise AppException("Something went wrong", 500)

def get_all(db: Session):
    logger.info("Fetching all addresses")
    return db.query(Address).all()


def get_by_id(db: Session, address_id: int):
    logger.info(f"Fetching address with id={address_id}")
    return db.query(Address).filter(Address.id == address_id).first()


def update(db: Session, db_address, update_data):
    try:
        update_dict = update_data.dict(exclude_unset=True)

        if not update_dict:
            raise AppException("No data provided for update", 400)

        for key, value in update_dict.items():
            setattr(db_address, key, value)

        db.commit()
        db.refresh(db_address)

        logger.info(f"Address updated successfully id={db_address.id}")
        return db_address
    
    except SQLAlchemyError as e:
        db.rollback()
        logger.exception("Database error while updating address")

        raise AppException("Database error occurred", 500)

    except AppException:
        db.rollback()
        raise

    except Exception as e:
        db.rollback()
        logger.exception(f"Unexpected error: {e}")

        raise AppException("Something went wrong", 500)

def delete(db: Session, db_address):
    try:
        db.delete(db_address)
        db.commit()
        logger.info(f"Address deleted successfully id={db_address.id}")
        return db_address
    except Exception as e:
        db.rollback()
        logger.exception(f"Error deleting address: {e}")
        raise