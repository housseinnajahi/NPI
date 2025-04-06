import logging

from fastapi import FastAPI

from . import models
from .postgres import postgres
from .router import router


def create_application() -> FastAPI:
    application = FastAPI(
        openapi_url="/calculator/openapi.json", docs_url="/calculator/docs"
    )
    application.include_router(router, prefix="/api/v1", tags=["calculator"])
    models.postgres.base.metadata.create_all(bind=postgres.engine)
    return application


app = create_application()
log = logging.getLogger("uvicorn")


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    log.info(url_list)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
