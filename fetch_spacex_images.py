import argparse
import os

import requests

from image_files_helpers import save_image

SPACEX_BASE_URL = "https://api.spacexdata.com"


class NoImagesException(Exception):
    pass


def fetch_spacex_last_launch(images_directory, launch_id="latest"):
    url = f"{SPACEX_BASE_URL}/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    if not links:
        raise NoImagesException("No images available for the given launch ID.")
    for key, link in enumerate(links):
        save_image(link, f"spacex_{key}.jpg", images_directory)
    return len(links)


def main():
    load_dotenv()
    images_directory = os.environ["IMAGES_DIRECTORY"]
    parser = argparse.ArgumentParser(
        description=(
            "Script for downloading SpaceX images"
            " from a specific launch or the latest."
        )
    )
    parser.add_argument(
        "launch_id",
        nargs="?",
        default="latest",
        help=("ID of launch, if not set - use latest"),
    )
    args = parser.parse_args()
    launch_id = args.launch_id
    try:
        downloaded_images_count = fetch_spacex_last_launch(
            images_directory,
            launch_id
        )
        print(f"Successfully downloaded {downloaded_images_count} images.")
    except NoImagesException as e:
        print(e)


if __name__ == "__main__":
    main()
