from fastapi import Request

from app.core.config import templates
from app.db import db_handler


def render_todo_card_list(
    request: Request,
):
    return templates.TemplateResponse(
        "partials/todo_card_list.html",
        {
            "request": request,
            "todo_items": db_handler.get_todo_items(),
            "should_hide_loader": True,
        },
    )
