def plan_actions(
    category: str,
    priority: str
):

    actions = [
        "create_ticket",
        "assign_team",
        "notify_customer",
        "notify_team"
    ]

    if priority == "High":

        actions.append(
            "manager_escalation"
        )

    return actions