from fastapi import APIRouter

from database.db import (
    SessionLocal
)

from database.repository import (
    save_ticket
)

from workflows.support_workflow import (
    run_workflow
)

from schemas.support_schema import (
    TranscriptRequest
)

from tools.notification_tool import (
    notify_customer,
    notify_team
)

from tools.verification_tool import (
    verify_workflow
)

from database.repository import (
    save_log
)

router = APIRouter()


@router.post("/Manual-Ticket")
def process_transcript(
    request: TranscriptRequest
):

    result = run_workflow(
        request.transcript
    )

    db = SessionLocal()

    save_ticket(

        db,

        result["ticket_id"],

        request.customer_email,

        result["intent"],

        result["category"],

        result["priority"],

        result["assigned_team"]
    )
    
    customer_status = notify_customer(

    request.customer_email,

    result["ticket_id"],

    result["assigned_team"],

    result["priority"]
    )

    save_log(

    db,

    result["ticket_id"],

    "notify_customer",

    "SUCCESS"
    )

    team_status = notify_team(

    result["ticket_id"],

    result["assigned_team"],

    result["category"]
    )

    save_log(

    db,

    result["ticket_id"],

    "notify_team",

    "SUCCESS"
    )

    workflow_status = verify_workflow(

    customer_status,

    team_status
    )

    save_log(

    db,

    result["ticket_id"],

    "verification",

    workflow_status
    )

    result["workflow_status"] = (
    workflow_status
    )

    return result