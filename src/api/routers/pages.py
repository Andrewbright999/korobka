from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=["Pages"],
)

templates = Jinja2Templates(directory="../templates")

@router.get("/admin")
def get_admin_page(request: Request) -> HTMLResponse:
    """Админ панель"""
    return templates.TemplateResponse("admin.html", {"request": request})

@router.get("/courier")
def get_admin_page(request: Request) -> HTMLResponse:
    """Страница для курьеров"""
    return templates.TemplateResponse("courier.html", {"request": request})

@router.get("/storage")
def get_storage_page(request: Request) -> HTMLResponse:
    """Главная страница, если пользователь не авторизован, то редирект на страницу входа"""
    return templates.TemplateResponse("storage.html", {"request": request})

@router.get("/login")
def get_login_page(request: Request) -> HTMLResponse:
    """Страница для входа"""
    context = {"request": request}
    return templates.TemplateResponse("index.html", {"request": request})
    
@router.get("/500")
def get_server_err_page(request: Request) -> HTMLResponse:
    """Страница ощибки сервера в демонстративных целях"""
    context = {"request": request}
    return templates.TemplateResponse("500.html", {"request": request})