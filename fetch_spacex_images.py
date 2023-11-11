import argparse

import requests

from image_files_helpers import save_image

SPACEX_BASE_URL = "https://api.spacexdata.com"


class NoImagesException(Exception):
    pass


def fetch_spacex_last_launch(launch_id="latest"):
    url = f"{SPACEX_BASE_URL}/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    if not links:
        raise NoImagesException("No images available for the given launch ID.")
    for key, link in enumerate(links):
        save_image(link, f"spacex_{key}.jpg")
    return len(links)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "launch_id",
        nargs='?',
        default="latest",
        help=(
            "ID of launch, if not set - use latest"
        )
    )
    try:
        args = parser.parse_args()
        launch_id = args.launch_id
        downloaded_images_count = fetch_spacex_last_launch(launch_id)
        print(f"Successfully downloaded {downloaded_images_count} images.")
    except NoImagesException as e:
        print(e)


if __name__ == "__main__":
    main()