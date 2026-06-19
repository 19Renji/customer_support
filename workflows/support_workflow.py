from agents.intent_agent import detect_intent
from agents.classification_agent import classify_issue
from agents.priority_agent import determine_priority
from agents.planner_agent import plan_actions

from tools.ticket_tool import create_ticket
from tools.assignment_tool import assign_team


def run_workflow(
    transcript
):

    intent = detect_intent(
        transcript
    )

    category = classify_issue(
        transcript
    )

    priority = determine_priority(
        transcript
    )

    actions = plan_actions(
        category,
        priority
    )

    ticket_id = create_ticket()

    team = assign_team(
        category
    )

    return {

        "ticket_id":
            ticket_id,

        "intent":
            intent,

        "category":
            category,

        "priority":
            priority,

        "assigned_team":
            team,

        "actions":
            actions
    }