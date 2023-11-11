import os
import urllib
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()
IMAGES_DIRECTORY = os.path.join(os.getcwd(), os.environ["IMAGES_DIRECTORY"])


def save_image(url, filename, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f"{IMAGES_DIRECTORY}/{filename}", "wb") as file:
        file.write(response.content)


def get_file_extension(url):
    path = urllib.parse.urlparse(url).path
    return os.path.splitext(path)[1].lower()


def get_images():
    images_files = []
    for filename in os.listdir(IMAGES_DIRECTORY):
        if get_file_extension(filename) in (".png", ".jpg", ".jpeg"):
            images_files.append(f"{IMAGES_DIRECTORY}/{filename}")
    return images_files


Path(IMAGES_DIRECTORY).mkdir(parents=True, exist_ok=True)
