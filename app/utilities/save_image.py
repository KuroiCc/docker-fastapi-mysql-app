from pathlib import Path
import time

from fastapi import UploadFile
import pyheif
from PIL import Image
import shutil


def save_image(image: UploadFile, save_dir: str = 'images', filename: str = str(time.time())):
    root_dir = Path('app/statics')
    save_dir = Path(save_dir)

    def get_sava_path():
        return root_dir / str(save_dir)

    if not get_sava_path().exists():
        get_sava_path().mkdir(parents=True)

    suffix = Path(image.filename).suffix
    fileobj = image.file
    # ios画像対応しない場合はここいらない
    if suffix == '.heic' or suffix == '.HEIC':
        heif_file = pyheif.read(fileobj)
        data = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        save_dir = save_dir / f'{filename}.jpeg'
        data.save(str(get_sava_path().resolve()), "JPEG")
    else:
        save_dir = save_dir / f'{filename}{suffix}'
        with get_sava_path().open('wb+') as f:
            shutil.copyfileobj(fileobj, f)

    return f"/{save_dir}"
