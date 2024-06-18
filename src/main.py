import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from boxes.router import router as box_router
from auth.routers import router as auth_router
from pages.router import router as page_router
from auth.admin import create_admin


app = FastAPI(
    title="Коробка"
)
app.config["PREFERRED_URL_SCHEME"] = "https"

app.include_router(auth_router)
app.include_router(box_router)
app.include_router(page_router)

app.mount("/static", StaticFiles(directory="../static"), name="static")

# origins = [
#     # "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
#                    "Authorization"],
# )


# @app.middleware("http")
# async def auth_middleware(request, call_next):
#     response = await call_next(request)
#     if response.status_code == 401:
#         return RedirectResponse(url="/login", status_code=302)



@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        pass
        # await conn.run_sync(Base.metadata.drop_all)
        # await conn.run_sync(Base.metadata.create_all)
    await create_admin()


# @app.get("/")
# async def login_page():
#     return RedirectResponse(url="/login")
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)