from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Secure", "version": "1.0.0"}