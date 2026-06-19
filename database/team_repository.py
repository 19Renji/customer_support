from database.models import Team


def get_team_by_name(
    db,
    team_name
):

    return (

        db.query(Team)

        .filter(
            Team.team_name == team_name
        )

        .first()
    )