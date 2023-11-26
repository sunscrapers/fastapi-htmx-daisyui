from fastapi import APIRouter

from app.views.health import router as health_router

main_router = APIRouter()

main_router.include_router(health_router)
