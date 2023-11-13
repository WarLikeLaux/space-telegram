import os
import urllib
from pathlib import Path

import requests
from dotenv import load_dotenv


def save_image(url, filename, images_directory, params={}):
    images_directory_abs_path = os.path.join(
        os.getcwd(),
        images_directory
    )
    Path(images_directory_abs_path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f"{images_directory_abs_path}/{filename}", "wb") as file:
        file.write(response.content)


def get_file_extension(url):
    path = urllib.parse.urlparse(url).path
    return os.path.splitext(path)[1].lower()


def get_images(images_directory):
    images_directory_abs_path = os.path.join(
        os.getcwd(),
        images_directory
    )
    Path(images_directory_abs_path).mkdir(parents=True, exist_ok=True)
    images_files = []
    for filename in os.listdir(images_directory_abs_path):
        if get_file_extension(filename) in (".png", ".jpg", ".jpeg"):
            images_files.append(f"{images_directory_abs_path}/{filename}")
    return images_files
