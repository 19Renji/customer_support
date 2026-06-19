from database.db import SessionLocal
from database.models import Team

db = SessionLocal()

teams = [

    Team(
        team_name="Authentication Team",
        team_email="authsupport@gmail.com",
        manager_email="authmanager@gmail.com"
    ),

    Team(
        team_name="Billing Team",
        team_email="billingsupport@gmail.com",
        manager_email="billingmanager@gmail.com"
    ),

    Team(
        team_name="Technical Support Team",
        team_email="techsupport@gmail.com",
        manager_email="techmanager@gmail.com"
    ),

    Team(
        team_name="Customer Care Team",
        team_email="customersupport@gmail.com",
        manager_email="caremanager@gmail.com"
    )
]

for team in teams:

    db.add(team)

db.commit()

print("Teams Added")