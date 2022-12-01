from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preço_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2l", "preço_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750", "preço_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preço_unitario": 2, "quantidade": 5},
}


@app.get('/')
async def home():  # raiz pode ser qualquer nome
    return {"vendas": len(vendas)}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# id_vendas é variavel então tem que vir entre colchetes
# dartipagem para id


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente"}
