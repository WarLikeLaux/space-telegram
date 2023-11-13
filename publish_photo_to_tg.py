import argparse
import os
import random

import telegram
from dotenv import load_dotenv

from image_files_helpers import get_images


def main():
    load_dotenv()
    bot_token = os.environ["TG_BOT_TOKEN"]
    channel_id = os.environ["TG_CHANNEL_ID"]
    images_directory = os.environ["IMAGES_DIRECTORY"]
    bot = telegram.Bot(token=bot_token)
    parser = argparse.ArgumentParser(
        description=(
            "Script for publishing a specific or random photo"
            " from the images dDirectory to a telegram channel."
        )
    )
    parser.add_argument(
        "photo_path",
        nargs="?",
        type=str,
        help=(
            "Specify a photo path to publish."
            " Leave empty to publish a random photo."
        ),
    )
    args = parser.parse_args()
    if args.photo_path:
        photo_path = args.photo_path
    else:
        photo_path = random.choice(get_images(images_directory))
    with open(photo_path, "rb") as photo:
        bot.send_photo(chat_id=channel_id, photo=photo)
    print(
        f"Successfully published {photo_path}"
        f" to the Telegram channel with ID {channel_id}."
    )


if __name__ == "__main__":
    main()
