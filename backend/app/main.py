from fastapi import FastAPI

app = FastAPI(title="Anonymous File Transfer")


@app.get("/")
def root():
    return {
        "message": "Anonymous File Transfer API is running"
    }