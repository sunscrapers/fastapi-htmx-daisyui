from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.core import config
from app.routes import main_router


def get_application() -> FastAPI:
    application = FastAPI(title=config.PROJECT_NAME, debug=config.DEBUG)

    # CORS protection
    application.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(main_router)
    application.mount(
        "/static",
        StaticFiles(directory="app/static"),
        name="static",
    )

    return application


app = get_application()

if __name__ == "__main__":
    import uvicorn

    kwargs = {"host": "0.0.0.0", "port": 8000}

    if config.DEBUG is True:
        kwargs.update({"reload": True, "reload_dirs": [".."]})

    uvicorn.run("app.main:app", **kwargs)
