from fastapi import FastAPI
from lemon_webhook import router as lemon_router

app = FastAPI()
app.include_router(lemon_router)

@app.get("/")
def read_root():
    return {"message": "MyNews AI Backend is live."}
