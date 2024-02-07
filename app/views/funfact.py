import asyncio
import logging
from typing import Annotated
from typing import Dict
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import templates
from app.dependencies.db import get_db
from app.models.funfact import FunFact

logger = logging.getLogger(__name__)

PAGINATE_BY_FUN_FACT: int = 3
router = APIRouter()


# Full load
@router.get("/fun-fact-full-load", response_class=HTMLResponse)
async def fun_fact_full_load(
    request: Request,
    db_session: Annotated[AsyncSession, Depends(get_db)],
):
    # Fetch Fun Facts rows
    result = await db_session.execute(
        select(
            FunFact.title,
            FunFact.description,
        )
        .order_by(func.random())
        .limit(PAGINATE_BY_FUN_FACT),
    )
    fun_facts: List[Dict[str, str]] = result.mappings().all()

    # Header - Fetch Fun Facts count
    result = await db_session.execute(select(func.count(FunFact.id)))
    fun_facts_count: int = result.fetchone()[0]

    # Footer - Fake waiting for external resources
    await asyncio.sleep(1)

    return templates.TemplateResponse(
        "pages/funfact_full_load.html",
        {
            "request": request,
            "fun_facts": fun_facts,
            "fun_facts_count": fun_facts_count,
        },
    )


# Partial load
@router.get("/fun-fact-partial-load", response_class=HTMLResponse)
async def fun_fact_partial_load(request: Request):
    return templates.TemplateResponse(
        "pages/funfact_partial_load.html",
        {
            "request": request,
        },
    )


@router.get("/fun-fact-partial-load-count", response_class=HTMLResponse)
async def fun_fact_partial_load_count(
    request: Request,
    db_session: Annotated[AsyncSession, Depends(get_db)],
):
    logger.warning("Started partial load for fun facts count")
    # Fetch Fun Facts count
    result = await db_session.execute(select(func.count(FunFact.id)))
    fun_facts_count: int = result.fetchone()[0]

    return templates.TemplateResponse(
        "partials/funfact_count.html",
        {
            "request": request,
            "fun_facts_count": fun_facts_count,
        },
    )


@router.get("/fun-fact-partial-load-footer", response_class=HTMLResponse)
async def fun_fact_partial_load_footer(request: Request):
    logger.warning("Started partial load for footer")
    # Footer - Fake waiting for external resources
    await asyncio.sleep(1)

    return templates.TemplateResponse(
        "partials/funfact_footer.html",
        {
            "request": request,
        },
    )


@router.get("/fun-fact-partial-load-data", response_class=HTMLResponse)
async def fun_fact_partial_load_data(
    request: Request,
    db_session: Annotated[AsyncSession, Depends(get_db)],
):
    logger.warning("Started partial load for data")
    # Fetch Fun Facts rows
    result = await db_session.execute(
        select(
            FunFact.title,
            FunFact.description,
        )
        .order_by(func.random())
        .limit(PAGINATE_BY_FUN_FACT),
    )
    fun_facts: List[Dict[str, str]] = result.mappings().all()

    return templates.TemplateResponse(
        "partials/funfacts.html",
        {
            "request": request,
            "fun_facts": fun_facts,
        },
    )
