from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import secrets
import string
import os
import shutil

app = FastAPI(title="Anonymous File Transfer")

# Fixing Cors Error - Cors = error when connecting frontend and backend, because both have different links
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def generate_drop_id(length: int = 8) -> str:
    characters = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


def generate_file_id() -> str:
    return secrets.token_urlsafe(16)


@app.get("/")
def root():
    return {
        "message": "Anonymous File Transfer API is running"
    }


@app.post("/drops")
def create_drop():
    drop_id = generate_drop_id()

    drop_folder = os.path.join(UPLOAD_DIR, drop_id)
    os.makedirs(drop_folder, exist_ok=True)

    return {
        "drop_id": drop_id
    }


@app.post("/drops/{drop_id}/files")
def upload_file(
    drop_id: str,
    file: UploadFile = File(...)
):
    drop_folder = os.path.join(UPLOAD_DIR, drop_id)

    if not os.path.exists(drop_folder):
        raise HTTPException(
            status_code=404,
            detail="Drop not found"
        )

    file_id = generate_file_id()

    filename = os.path.basename(file.filename)

    file_path = os.path.join(
        drop_folder,
        f"{file_id}_{filename}"
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "drop_id": drop_id,
        "file_id": file_id,
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

    for stored_filename in os.listdir(drop_folder):
        file_path = os.path.join(drop_folder, stored_filename)

        if os.path.isfile(file_path):

            file_id, filename = stored_filename.split("_", 1)

            files.append({
                "file_id": file_id,
                "filename": filename
            })

    return {
        "drop_id": drop_id,
        "files": files
    }


@app.get("/files/{file_id}/download")
def download_file(file_id: str):
    for drop_id in os.listdir(UPLOAD_DIR):

        drop_folder = os.path.join(UPLOAD_DIR, drop_id)

        if not os.path.isdir(drop_folder):
            continue

        for stored_filename in os.listdir(drop_folder):

            if stored_filename.startswith(file_id + "_"):

                file_path = os.path.join(
                    drop_folder,
                    stored_filename
                )

                filename = stored_filename.split("_", 1)[1]

                from fastapi.responses import FileResponse

                return FileResponse(
                    path=file_path,
                    filename=filename,
                    media_type="application/octet-stream"
                )

    raise HTTPException(
        status_code=404,
        detail="File not found"
    )