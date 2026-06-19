def assign_team(category):

    category = category.lower()

    if (
        "login" in category
        or
        "authentication" in category
        or
        "account access" in category
        or
        "account" in category
    ):
        return "Authentication Team"

    elif (
        "payment" in category
        or
        "billing" in category
        or
        "refund" in category
    ):
        return "Billing Team"

    elif (
        "technical" in category
        or
        "system" in category
        or
        "bug" in category
    ):
        return "Technical Support Team"

    return "Customer Care Team"