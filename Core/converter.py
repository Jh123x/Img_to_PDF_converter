import os
from PIL import Image

from Core.constants import NO_FILES_SELECTED, OUTPUT_FOLDER, OUTPUT_PATH, PDF_FORMAT, RGB_FORMAT, SUCCESS_MESSAGE


def convert_file(file_path: str) -> str:
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


def convert_files(file_paths: tuple) -> str:
    """Convert the file at the locations to multiple PDFs"""
    if len(file_paths) == 0:
        return NO_FILES_SELECTED

    failed = 0
    for path in file_paths:
        try:
            convert_file(path)
        except FileNotFoundError:
            failed += 1

    return SUCCESS_MESSAGE.format(len(file_paths) - failed, failed)
