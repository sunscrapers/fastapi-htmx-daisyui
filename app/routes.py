from fastapi import APIRouter

from app.views.funfact import router as funfact_router
from app.views.health import router as health_router
from app.views.home import router as home_router
from app.views.todo import router as todo_router

main_router = APIRouter()


main_router.include_router(health_router)
main_router.include_router(home_router)
main_router.include_router(todo_router)
main_router.include_router(funfact_router)
