from typing import TypedDict


class SupportState(TypedDict):

    transcript: str

    intent: str

    category: str

    priority: str

    actions: list

    ticket_id: str

    assigned_team: str

    customer_email_status: bool

    team_email_status: bool

    workflow_status: str

    retry_count: int

    customer_email: str