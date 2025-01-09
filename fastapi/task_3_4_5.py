from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def fastapi_hello():
    return {"message": "Hello, nfactorial!"}

@app.post("/fastapi-meaning-life")
def fastapi_meaning_life():
    return  {"meaning": "42"}

@app.get("/{num}")
def fastapi_nfactorial(num:int):
    return {"nfactorial": recursive_factorial(num)}

def recursive_factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return  n*recursive_factorial(n-1)