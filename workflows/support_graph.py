from langgraph.graph import StateGraph
from workflows.state import SupportState

from agents.intent_agent import detect_intent
from agents.classification_agent import classify_issue
from agents.priority_agent import determine_priority
from agents.planner_agent import plan_actions

from tools.ticket_tool import create_ticket
from tools.assignment_tool import assign_team

from database.repository import (
    save_ticket,
    save_log
)


def intent_node(
    state: SupportState
):

    state["intent"] = detect_intent(
        state["transcript"]
    )

    return state

def classification_node(
    state: SupportState
):

    state["category"] = classify_issue(
        state["transcript"]
    )

    return state


def priority_node(
    state: SupportState
):

    state["priority"] = determine_priority(
        state["transcript"]
    )

    return state

def planner_node(
    state: SupportState
):

    state["actions"] = plan_actions(
        state["category"],
        state["priority"]
    )

    return state

def ticket_node(
    state: SupportState
):

    state["ticket_id"] = (
        create_ticket()
    )

    return state

def assignment_node(
    state: SupportState
):

    state["assigned_team"] = (
        assign_team(
            state["category"]
        )
    )

    return state

from tools.notification_tool import (
    notify_customer,
    notify_team
)

def notification_node(
    state: SupportState
):

    customer_status = notify_customer(

        state["customer_email"],

        state["ticket_id"],

        state["assigned_team"],

        state["priority"]
    )

    team_status = notify_team(

        state["ticket_id"],

        state["assigned_team"],

        state["category"]
    )

    state["customer_email_status"] = (
        customer_status
    )

    state["team_email_status"] = (
        team_status
    )

    return state

from tools.verification_tool import (
    verify_workflow
)

def verification_node(
    state: SupportState
):

    status = verify_workflow(

        state["customer_email_status"],

        state["team_email_status"]
    )

    state["workflow_status"] = (
        status
    )

    return state

from database.db import (
    SessionLocal
)

from database.repository import (
    save_log
)

def logging_node(
    state: SupportState
):

    db = SessionLocal()

    save_log(

        db,

        state["ticket_id"],

        "workflow_completed",

        state["workflow_status"]
    )

    return state

def retry_decision(
    state: SupportState
):

    if (
        state["workflow_status"]
        ==
        "FAILED"
    ):

        return "retry"

    return "success"

def save_ticket_node(
    state: SupportState
):

    db = SessionLocal()

    save_ticket(

        db,

        state["ticket_id"],

        state["customer_email"],

        state["intent"],

        state["category"],

        state["priority"],

        state["assigned_team"]
    )

    return state

graph = StateGraph(
    SupportState
)
graph.add_node(
    "intent",
    intent_node
)

graph.add_node(
    "classification",
    classification_node
)

graph.add_node(
    "priority",
    priority_node
)

graph.add_node(
    "planner",
    planner_node
)

graph.add_node(
    "ticket",
    ticket_node
)

graph.add_node(
    "assignment",
    assignment_node
)
graph.add_node(
    "notification",
    notification_node
)

graph.add_node(
    "verification",
    verification_node
)

graph.add_node(
    "logging",
    logging_node
)

graph.add_node(
    "save_ticket",
    save_ticket_node
)

graph.set_entry_point(
    "intent"
)

graph.add_edge(
    "intent",
    "classification"
)

graph.add_edge(
    "classification",
    "priority"
)

graph.add_edge(
    "priority",
    "planner"
)

graph.add_edge(
    "planner",
    "ticket"
)

graph.add_edge(
    "ticket",
    "assignment"
)

graph.add_edge(
    "assignment",
    "save_ticket"
)

graph.add_edge(
    "save_ticket",
    "notification"
)

graph.add_edge(
    "notification",
    "verification"
)

graph.add_conditional_edges(

    "verification",

    retry_decision,

    {

        "retry":
            "notification",

        "success":
            "logging"
    }
)

graph.set_finish_point(
    "logging"
)

support_graph = (
    graph.compile()
)