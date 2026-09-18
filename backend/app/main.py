from fastapi import FastAPI
import secrets
import string

app = FastAPI(title="Anonymous File Transfer")


def generate_drop_id(length: int = 8) -> str:
    characters = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


@app.get("/")
def root():
    return {
        "message": "Anonymous File Transfer API is running"
    }


@app.post("/drops")
def create_drop():
    drop_id = generate_drop_id()

    return {
        "drop_id": drop_id
    }