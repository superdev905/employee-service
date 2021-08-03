
import os
import mimetypes
import shutil
from tempfile import NamedTemporaryFile
import aiofiles
from fastapi import APIRouter, File, UploadFile
from fastapi.param_functions import Path
from fastapi import HTTPException, status
from fastapi.responses import FileResponse


router = APIRouter(prefix="/file", tags=["Files"])


PATH = '.'


def search_File(fileName):
    for root, dirs, files in os.walk(PATH):
        for Files in files:
            try:
                found = Files.find(fileName)

                if found != -1:
                    return found
            except:
                exit()


@router.post("")
async def create_file(file: UploadFile = File(...)):

    file_location = f"{file.filename}"
    with open(file_location, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)

    return {"filename": file.filename, "target": file_location}


@router.get("/{file_key}")
def get_file(file_key: str):

    file = os.path.join("./", file_key)
    print(file)
    return FileResponse(file)
