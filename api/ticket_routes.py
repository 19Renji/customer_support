from fastapi import APIRouter, HTTPException

from database.db import SessionLocal

from database.models import Ticket

from database.repository import (
    get_ticket_by_id,
    update_ticket_status
)

from schemas.status_schema import (
    StatusUpdate
)

router = APIRouter()


@router.get("/tickets")
def get_tickets():

    db = SessionLocal()

    return db.query(
        Ticket
    ).all()


@router.get(
    "/tickets/{ticket_id}"
)
def get_ticket(
    ticket_id: str
):

    db = SessionLocal()

    ticket = get_ticket_by_id(
        db,
        ticket_id
    )

    if not ticket:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.patch(
    "/tickets/{ticket_id}/status"
)
def update_status(

    ticket_id: str,

    request: StatusUpdate

):

    db = SessionLocal()

    ticket = update_ticket_status(

        db,

        ticket_id,

        request.status
    )

    if not ticket:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket