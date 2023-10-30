import os
import urllib
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

IMAGES_DIRECTORY = "images"
SPACEX_BASE_URL = "https://api.spacexdata.com"
NASA_API_KEY = os.environ['NASA_API_KEY']
NASA_BASE_URL = "https://api.nasa.gov"


def save_image(url, filename, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f"{IMAGES_DIRECTORY}/{filename}", 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = f"{SPACEX_BASE_URL}/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for key, link in enumerate(links):
        save_image(link, f"spacex_{key}.jpg")


def get_file_extension(url):
    path = urllib.parse.urlparse(url).path
    return os.path.splitext(path)[1]


def get_nasa_available_dates(count):
    params = {
        "api_key": NASA_API_KEY,
    }
    url = f"{NASA_BASE_URL}/EPIC/api/natural/available"
    response = requests.get(url, params=params)
    response.raise_for_status()
    dates = response.json()
    return dates[-count:]


def get_nasa_epic(count):
    dates = get_nasa_available_dates(count)
    params = {
        "api_key": NASA_API_KEY,
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


def get_nasa_apod(count):
    params = {
        "api_key": NASA_API_KEY,
        "count": count,
    }
    url = f"{NASA_BASE_URL}/planetary/apod"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for key, image in enumerate(images):
        if "hdurl" in image:
            hdurl = image['hdurl']
            extension = get_file_extension(hdurl)
            save_image(hdurl, f"nasa_apod_{key}{extension}")


def main():
    Path(IMAGES_DIRECTORY).mkdir(parents=True, exist_ok=True)
    # fetch_spacex_last_launch()
    # get_nasa_apod(5)
    # get_nasa_epic(5)


if __name__ == "__main__":
    main()
