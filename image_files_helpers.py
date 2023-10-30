import os
import urllib
from pathlib import Path

import requests

IMAGES_DIRECTORY = "images"


def save_image(url, filename, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f"{IMAGES_DIRECTORY}/{filename}", 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    path = urllib.parse.urlparse(url).path
    return os.path.splitext(path)[1]


Path(IMAGES_DIRECTORY).mkdir(parents=True, exist_ok=True)
