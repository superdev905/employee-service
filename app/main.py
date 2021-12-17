from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.API.v1.router import router as V1_Routes, public_router as V1_Public_routes
from app.API.v1.seeds.init import seed_base_data
from app.database.main import get_database

app = FastAPI(title="Servicio de trabajadores")

app.include_router(V1_Routes, prefix="/api/v1")
app.include_router(V1_Public_routes, prefix="/api/v1/public")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup():
    get_database()
    seed_base_data()
