from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/health", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "pages/health.html",
        {"request": request},
    )
