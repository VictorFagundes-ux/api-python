from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    return {"mensagem":"Hello World"}

@app.get("/teste")
async def teste():
    return {"mensagem":"testando"}