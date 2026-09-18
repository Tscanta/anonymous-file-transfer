from fastapi import FastAPI, UploadFile, File, HTTPException
import secrets
import string
import os
import shutil

app = FastAPI(title="Anonymous File Transfer")


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


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


@app.post("/drops/{drop_id}/files")
def upload_file(
    drop_id: str,
    file: UploadFile = File(...)
):
    filename = os.path.basename(file.filename)

    drop_folder = os.path.join(UPLOAD_DIR, drop_id)
    os.makedirs(drop_folder, exist_ok=True)

    file_path = os.path.join(drop_folder, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "drop_id": drop_id,
        "filename": filename
    }

@app.get("/drops/{drop_id}")
def get_drop(drop_id: str):
    drop_folder = os.path.join(UPLOAD_DIR, drop_id)

    if not os.path.exists(drop_folder):
        raise HTTPException(
            status_code=404,
            detail="Drop not found"
        )

    files = []

    for filename in os.listdir(drop_folder):
        file_path = os.path.join(drop_folder, filename)

        if os.path.isfile(file_path):
            files.append({
                "filename": filename
            })

    return {
        "drop_id": drop_id,
        "files": files
    }