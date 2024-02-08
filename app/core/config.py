from typing import List

from fastapi.templating import Jinja2Templates
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

PROJECT_NAME = config(
    "PROJECT_NAME",
    default="FastAPI, HTMX, Jinja2, Tailwind CSS + DaisyUI, Docker - Showcase",
)
SECRET_KEY = config("SECRET_KEY", default="secret")

DEBUG = config("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="")

templates = Jinja2Templates(directory="app/templates")

# Database
DATABASE_URL = config("DATABASE_URL", default="postgresql+asyncpg://postgres:postgres@db:5432/mydatabase")
