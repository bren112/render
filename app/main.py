from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando no Railway 🎉"}

@app.get("/ping")
def ping():
    return {"pong ❇️": True}
