from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "Server is up and running ✅"}
