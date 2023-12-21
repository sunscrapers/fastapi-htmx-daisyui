import time
from typing import Annotated

from fastapi import APIRouter
from fastapi import Form
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.core.config import templates
from app.db import db_handler
from app.utils import render_todo_card_list

router = APIRouter()


@router.get("/todo", response_class=HTMLResponse)
async def todo_view(request: Request):
    return templates.TemplateResponse(
        "pages/todo_app.html",
        {"request": request},
    )


@router.get("/todo/list", response_class=HTMLResponse)
async def todo_list(request: Request):
    time.sleep(2)  # to slow down loading items and show loader
    return render_todo_card_list(request=request)


@router.post("/todo/add", response_class=HTMLResponse)
async def todo_add(request: Request, value: Annotated[str, Form()]):
    db_handler.add_todo_item(value=value)
    return render_todo_card_list(request=request)


@router.post("/todo/remove", response_class=HTMLResponse)
async def todo_remove(request: Request, item_id: Annotated[str, Form()]):
    db_handler.remove_todo_item(item_id=item_id)

    return render_todo_card_list(request=request)


@router.post("/todo/clear", response_class=HTMLResponse)
async def todo_clear(request: Request):
    db_handler.clear_todo_items()

    return render_todo_card_list(request=request)
