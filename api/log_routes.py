from fastapi import APIRouter

from database.db import SessionLocal

from database.repository import (
    get_logs_by_ticket
)

router = APIRouter()


@router.get(
    "/logs/{ticket_id}"
)
def get_logs(
    ticket_id: str
):

    db = SessionLocal()

    return get_logs_by_ticket(
        db,
        ticket_id
    )