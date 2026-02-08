from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Shopify Inventory Sync")

app.include_router(router)