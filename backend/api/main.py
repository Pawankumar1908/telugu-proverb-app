from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router
from api.auth import router as auth_router

app = FastAPI()

# CORS (needed for frontend hosting)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "API running"}
