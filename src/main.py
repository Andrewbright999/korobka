import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
from boxes.router import router as box_router
from auth.routers import router as auth_router
from pages.router import router as page_router
from auth.admin import create_admin




@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await create_admin()    
    yield

app = FastAPI(
    title="Коробка",
    lifespan=lifespan
)

app.include_router(auth_router)
app.include_router(box_router)
app.include_router(page_router)


app.mount("/static", StaticFiles(directory="../static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


templates = Jinja2Templates(directory="../templates")


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    """Обработка ошибки 404"""
    context = {"request": request}
    return templates.TemplateResponse("404.html", context=context)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Обработка некоректного ввода"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.exception_handler(500)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    """Обработка ошибки 500"""
    context = {"request": request}
    return templates.TemplateResponse("500.html", context=context)


@app.get("/")
async def default_page():
    """Переадресация на страницу склада"""
    return RedirectResponse(url="/storage")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)