from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()

SAVE_PATH = "C:/Users/nicki/Desktop/VanyaProject/coach_pictures"

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


@app.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    saved_file_path = os.path.join(SAVE_PATH, file.filename)

    with open(saved_file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"full_path": saved_file_path}