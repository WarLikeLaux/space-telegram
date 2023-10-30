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


def get_nasa_epic(api_key, count=5):
    dates = get_nasa_available_dates(api_key, count)
    params = {
        "api_key": api_key,
    }
    for key, date in enumerate(dates):
        url = f"{NASA_BASE_URL}/EPIC/api/natural/date/{date}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        image_id = data[0]['image']
        date = date.replace('-', '/')
        image_url = (
          f"{NASA_BASE_URL}/EPIC/archive/natural/{date}/png/{image_id}.png"
        )
        save_image(image_url, f"nasa_epic_{key}.png", params)
    return len(dates)


def main():
    load_dotenv()
    NASA_API_KEY = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "count",
        nargs='?',
        default=5,
        type=int,
        help=(
            "Count of need EPIC images to download"
        )
    )
    args = parser.parse_args()
    count = args.count
    downloaded_images_count = get_nasa_epic(NASA_API_KEY, count)
    print(f"Successfully downloaded {downloaded_images_count} images.")


if __name__ == "__main__":
    main()
