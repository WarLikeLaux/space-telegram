import argparse
import os

import requests
from dotenv import load_dotenv

from image_files_helpers import get_file_extension, save_image

NASA_BASE_URL = "https://api.nasa.gov"


def get_nasa_apod(api_key, count=5):
    params = {
        "api_key": api_key,
        "count": count,
    }
    url = f"{NASA_BASE_URL}/planetary/apod"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for key, image in enumerate(images):
        if "hdurl" in image:
            hdurl = image["hdurl"]
            extension = get_file_extension(hdurl)
            save_image(hdurl, f"nasa_apod_{key}{extension}")
    return len(images)


def main():
    load_dotenv()
    NASA_API_KEY = os.environ["NASA_API_KEY"]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "count",
        nargs="?",
        default=5,
        help=("Count of need APOD images to download")
    )
    args = parser.parse_args()
    count = args.count
    downloaded_images_count = get_nasa_apod(NASA_API_KEY, count)
    print(f"Successfully downloaded {downloaded_images_count} images.")


if __name__ == "__main__":
    main()
