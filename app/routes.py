from fastapi import APIRouter
from fastapi import status
from fastapi.responses import RedirectResponse

from app.views.health import router as health_router
from app.views.todo import router as todo_router

main_router = APIRouter()


@main_router.get("/")
async def redirect_todo():
    return RedirectResponse(url="/todo", status_code=status.HTTP_302_FOUND)


main_router.include_router(health_router)
main_router.include_router(todo_router)
