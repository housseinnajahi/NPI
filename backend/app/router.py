from fastapi import APIRouter

from .apis.apis import router as calculator_router

router = APIRouter()

router.include_router(calculator_router, prefix="/expressions", tags=["expressions"])
