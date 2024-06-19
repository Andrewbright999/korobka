from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=["Pages"],
)

templates = Jinja2Templates(directory="../templates")

@router.get("/storage")
def get_base_page(request: Request):
    return templates.TemplateResponse("storage.html", {"request": request})

@router.get("/login")
def get_base_page(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", {"request": request})
    
    


# @router.get("/test-login")
# def get_base_page(request: Request):
#     context = {"request": request}
#     return templates.TemplateResponse("test_login.html", context=context)

# @router.get("/profile")
# def get_base_page(request: Request):
#     context = {"request": request}
#     return templates.TemplateResponse("profile_page.html", context=context)

# @router.get("/search")
# def get_base_page(request: Request):
#     return templates.TemplateResponse("search.html", {"request": request})  