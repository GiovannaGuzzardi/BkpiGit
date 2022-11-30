from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def raiz():  # raiz pode ser qualquer nome
    return {"message": "Hello World"}

if __name__ == '__main__':
    import uvicorn

# 0.0.0.1 para qualquer pessoas na rede acessar
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
