from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.address import AddressCreate, AddressUpdate, AddressResponse
from app.services import address_service
from app.repositories import address_repository

router = APIRouter()


@router.post("/", response_model=AddressResponse)
def create(address: AddressCreate, db: Session = Depends(get_db)):
    return address_service.create_address(db, address)


@router.get("/", response_model=list[AddressResponse])
def get_all(db: Session = Depends(get_db)):
    return address_repository.get_all(db)


@router.get("/search", response_model=list[AddressResponse])
def search(lat: float,lon: float,distance_km: float,db: Session = Depends(get_db)):
    return address_service.get_addresses_within_distance(
        db, lat, lon, distance_km
    )


@router.put("/{address_id}", response_model=AddressResponse)
def update(address_id: int, data: AddressUpdate, db: Session = Depends(get_db)):
    return address_service.update_address(db, address_id, data)


@router.delete("/{address_id}")
def delete(address_id: int, db: Session = Depends(get_db)):
    address_service.delete_address(db, address_id)
    return {"message": "Deleted successfully"}