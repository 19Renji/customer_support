from fastapi import APIRouter

from database.db import SessionLocal
from database.models import Team

router = APIRouter()

@router.get("/teams")
def get_teams():

    db = SessionLocal()

    return db.query(
        Team
    ).all()