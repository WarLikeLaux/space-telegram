import os
import urllib
from pathlib import Path
import requests
from dotenv import load_dotenv


def initialize_module():
    load_dotenv()
    global IMAGES_DIRECTORY
    IMAGES_DIRECTORY = os.path.join(
        os.getcwd(), os.environ["IMAGES_DIRECTORY"]
    )
    Path(IMAGES_DIRECTORY).mkdir(parents=True, exist_ok=True)


def module_function_wrapper(func):
    def wrapper(*args, **kwargs):
        initialize_module()
        return func(*args, **kwargs)
    return wrapper


@module_function_wrapper
def save_image(url, filename, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f"{IMAGES_DIRECTORY}/{filename}", "wb") as file:
        file.write(response.content)


@module_function_wrapper
def get_file_extension(url):
    path = urllib.parse.urlparse(url).path
    return os.path.splitext(path)[1].lower()


@module_function_wrapper
def get_images():
    images_files = []
    for filename in os.listdir(IMAGES_DIRECTORY):
        if get_file_extension(filename) in (".png", ".jpg", ".jpeg"):
            images_files.append(f"{IMAGES_DIRECTORY}/{filename}")
    return images_files
