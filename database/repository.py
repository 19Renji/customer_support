from database.models import Ticket,WorkflowLog
from tools.notification_tool import (
    send_resolution_email
)

def save_ticket(
    db,
    ticket_id,
    customer_email,
    intent,
    category,
    priority,
    team
):

    ticket = Ticket(

        ticket_id=ticket_id,

        customer_email=customer_email,

        intent=intent,

        category=category,

        priority=priority,

        assigned_team=team,

        status="OPEN"
    )

    db.add(ticket)

    db.commit()

    db.refresh(ticket)

    return ticket

def save_log(

    db,

    ticket_id,

    step,

    status

):

    log = WorkflowLog(

        ticket_id=ticket_id,

        step_name=step,

        status=status
    )

    db.add(log)

    db.commit()

    db.refresh(log)

    return log

def get_ticket_by_id(
    db,
    ticket_id
):

    return (

        db.query(Ticket)

        .filter(
            Ticket.ticket_id == ticket_id
        )

        .first()
    )

def update_ticket_status(
    db,
    ticket_id,
    status
):

    ticket = (

        db.query(Ticket)

        .filter(
            Ticket.ticket_id == ticket_id
        )

        .first()
    )

    if not ticket:

        return None

    ticket.status = status

    db.commit()

    db.refresh(ticket)

    if status.upper() == "CLOSED":

        send_resolution_email(

            ticket.customer_email,

            ticket.ticket_id,

            ticket.category
        )

    return ticket

def get_logs_by_ticket(
    db,
    ticket_id
):

    return (

        db.query(WorkflowLog)

        .filter(
            WorkflowLog.ticket_id == ticket_id
        )

        .all()
    )

