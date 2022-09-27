from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from gensim.models import word2vec, KeyedVectors

from schemas import SuccessMsg

app = FastAPI()
# app.include_router(route_todo.router)
# app.include_router(route_auth.router)
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
    import logging
    logging.info("hey")
    logging.info(wv["年金"])
    return {"message": str(wv["年金"])}


if __name__ == '__main__':
    wv = KeyedVectors.load_word2vec_format("ja_vectors.kv")
    uvicorn.run(app)
