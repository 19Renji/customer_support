from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime

Base = declarative_base()


class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ticket_id = Column(
        String,
        unique=True
    )

    customer_email = Column(
        String
    )

    intent = Column(
        String
    )

    category = Column(
        String
    )

    priority = Column(
        String
    )

    assigned_team = Column(
        String
    )

    status = Column(
        String,
        default="OPEN"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Team(Base):

    __tablename__ = "teams"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    team_name = Column(
        String,
        unique=True
    )

    team_email = Column(
        String
    )

    manager_email = Column(
        String
    )

class WorkflowLog(Base):

    __tablename__ = "workflow_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ticket_id = Column(String)

    step_name = Column(String)

    status = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )