from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.core.config import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    return templates.TemplateResponse(
        "pages/home.html",
        {"request": request},
    )
