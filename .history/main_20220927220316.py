from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from schemas import SuccessMsg

app = FastAPI()
app.include_router(route_todo.router)
app.include_router(route_auth.router)
origins = ['http://localhost:5000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "Welcome to Fast API"}
