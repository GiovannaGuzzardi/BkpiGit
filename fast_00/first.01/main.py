from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def raiz():  # raiz pode ser qualquer nome
    return {"message": "Hello World"}
