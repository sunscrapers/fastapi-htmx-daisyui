from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.core.config import templates

router = APIRouter()


@router.get("/health", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "pages/health.html",
        {"request": request},
    )
