import argparse
import os

import requests
from dotenv import load_dotenv

from image_files_helpers import get_file_extension, save_image

NASA_BASE_URL = "https://api.nasa.gov"


def get_nasa_apod(api_key, images_directory, count=5):
    url = f"{NASA_BASE_URL}/planetary/apod"
    params = {
        "api_key": api_key,
        "count": count,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for key, image in enumerate(images):
        if "hdurl" not in image:
            continue
        hd_image_url = image["hdurl"]
        extension = get_file_extension(hd_image_url)
        save_image(hd_image_url, f"nasa_apod_{key}{extension}", images_directory)
    return len(images)


def main():
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    images_directory = os.environ["IMAGES_DIRECTORY"]
    parser = argparse.ArgumentParser(
        description="Script for downloading NASA APOD images."
    )
    parser.add_argument(
        "count",
        nargs="?",
        default=5,
        help="Count of need APOD images to download, default is 5."
    )
    args = parser.parse_args()
    count = args.count
    downloaded_images_count = get_nasa_apod(nasa_api_key, images_directory, count)
    print(f"Successfully downloaded {downloaded_images_count} images.")


if __name__ == "__main__":
    main()
