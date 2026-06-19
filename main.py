from fastapi import FastAPI

from api.routes import router
from api.team_routes import router as team_router
from api.ticket_routes import router as ticket_router
from api.log_routes import (router as log_router)

app = FastAPI(
    title="Customer Support Agent"
)

app.include_router(router)

app.include_router(team_router)

app.include_router(ticket_router)

app.include_router(log_router)