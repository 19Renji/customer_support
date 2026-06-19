def verify_workflow(

    customer_status,

    team_status

):

    if (

        customer_status

        and

        team_status

    ):

        return "SUCCESS"

    return "FAILED"