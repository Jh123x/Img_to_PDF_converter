import os
from typing import Optional
from PIL import Image
from datetime import datetime

from Core.constants import COMBINE_SUCCESS_MESSAGE, COMBINED_FILENAME, NO_FILES_SELECTED, OUTPUT_FOLDER, OUTPUT_PATH, PDF_FORMAT, RGB_FORMAT, SUCCESS_MESSAGE, DATE_TIME_FORMAT


def _convert_file(file_path: str) -> str:
    """Convert 1 file into a PDF"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    output_folder = os.path.join(os.getcwd(), OUTPUT_FOLDER)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    output_name = OUTPUT_PATH.format(os.path.basename(file_path))
    with Image.open(file_path) as img:
        out_img = img.convert(RGB_FORMAT)
        out_img.save(
            os.path.join(output_folder, output_name),
            PDF_FORMAT,
            quality=100,
            save_all=True,
            optimize=True
        )
    return output_name


def _open_image(file_path: str) -> Optional[Image.Image]:
    """
    Open an image at the given file path
    First call to open
    Second call to close
    """
    if not os.path.exists(file_path):
        return None

    return Image.open(file_path)


def combine_all_files(file_paths: tuple[str]) -> str:
    """Combine all the files into one"""
    open_images = []
    fails = 0
    first = None

    # Open all the files
    for path in file_paths:
        try:
            old_img = _open_image(path)
            img = old_img.convert('RGB')
            old_img.close()
            if first is None:
                first = img
                continue
            open_images.append(img)
        except IOError:
            fails += 1

    # Get the output folder
    output_folder = os.path.join(
        os.getcwd(),
        OUTPUT_FOLDER,
        COMBINED_FILENAME.format(
            datetime.now().strftime(DATE_TIME_FORMAT)
        )
    )

    first.save(
        output_folder,
        PDF_FORMAT,
        quality=100,
        save_all=True,
        optimize=True,
        append_images=open_images
    )

    first.close()
    for img in open_images:
        img.close()

    return COMBINE_SUCCESS_MESSAGE.format(len(file_paths))


def convert_files(file_paths: tuple) -> str:
    """Convert the file at the locations to multiple PDFs"""
    if len(file_paths) == 0:
        return NO_FILES_SELECTED

    failed = 0
    for path in file_paths:
        try:
            _convert_file(path)
        except FileNotFoundError:
            failed += 1

    return SUCCESS_MESSAGE.format(len(file_paths) - failed, failed)
