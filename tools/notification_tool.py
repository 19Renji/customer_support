import smtplib

from email.message import EmailMessage

from config.settings import (
    EMAIL,
    APP_PASSWORD
)
from database.db import SessionLocal
from database.models import Team

def get_team_email(team_name):

    db = SessionLocal()

    team = (

        db.query(Team)

        .filter(
            Team.team_name == team_name
        )

        .first()
    )

    if team:

        return team.team_email

    return None


def notify_customer(

    customer_email,

    ticket_id,

    team,

    priority

):

    msg = EmailMessage()

    msg["Subject"] = (
        "Support Ticket Created"
    )

    msg["From"] = EMAIL

    msg["To"] = customer_email

    msg.set_content(
f"""
Ticket ID: {ticket_id}

Priority: {priority}

Assigned Team: {team}
"""
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL,
            APP_PASSWORD
        )

        smtp.send_message(msg)

    return True

def notify_team(

    ticket_id,

    team,

    category

):

    team_email = get_team_email(team)

    msg = EmailMessage()

    msg["Subject"] = (
        "New Ticket Assigned"
    )

    msg["From"] = EMAIL

    msg["To"] = team_email

    msg.set_content(
f"""
Ticket ID: {ticket_id}

Issue: {category}

Assigned Team: {team}
"""
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL,
            APP_PASSWORD
        )

        smtp.send_message(msg)

    return True

def send_resolution_email(
    customer_email,
    ticket_id,
    issue
):

    msg = EmailMessage()

    msg["Subject"] = (
        "Issue Resolved"
    )

    msg["From"] = EMAIL

    msg["To"] = customer_email

    msg.set_content(
    f"""
    Hello,

    Your support request has been successfully resolved.

    Ticket ID : {ticket_id}

    Issue : {issue}

    Status : CLOSED

    If you continue to face issues,
    please contact us again.

    Thank You,
    Customer Support Team
    """
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL,
            APP_PASSWORD
        )

        smtp.send_message(msg)

    return True