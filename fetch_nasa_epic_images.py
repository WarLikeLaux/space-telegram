import argparse
import os

import requests
from dotenv import load_dotenv

from image_files_helpers import save_image

NASA_BASE_URL = "https://api.nasa.gov"


def get_nasa_available_dates(api_key, count=5):
    params = {
        "api_key": api_key,
    }
    url = f"{NASA_BASE_URL}/EPIC/api/natural/available"
    response = requests.get(url, params=params)
    response.raise_for_status()
    dates = response.json()
    return dates[-count:]


def get_nasa_epic(api_key, images_directory, dates):
    params = {
        "api_key": api_key,
    }
    for key, date in enumerate(dates):
        url = f"{NASA_BASE_URL}/EPIC/api/natural/date/{date}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        image_id = response.json()[0]["image"]
        date_formatted = date.replace("-", "/")
        image_url = (
            f"{NASA_BASE_URL}/EPIC/archive/natural/"
            f"{date_formatted}/png/{image_id}.png"
        )
        save_image(image_url, f"nasa_epic_{key}.png", images_directory, params)
    return len(dates)


def main():
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    images_directory = os.environ["IMAGES_DIRECTORY"]
    parser = argparse.ArgumentParser(
        description="Script for downloading NASA EPIC images."
    )
    parser.add_argument(
        "count",
        nargs="?",
        default=5,
        type=int,
        help=("Count of need EPIC images to download, default is 5."),
    )
    args = parser.parse_args()
    count = args.count
    nasa_available_dates = get_nasa_available_dates(
        api_key=nasa_api_key,
        count=count
    )
    downloaded_images_count = get_nasa_epic(
        api_key=nasa_api_key,
        images_directory=images_directory,
        dates=nasa_available_dates
    )
    print(f"Successfully downloaded {downloaded_images_count} images.")


if __name__ == "__main__":
    main()
