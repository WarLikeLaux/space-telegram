import argparse
import os
import random

import telegram
from dotenv import load_dotenv

from image_files_helpers import get_images_from_path
from tg_helpers import publish_photo_to_channel


def main():
    load_dotenv()
    bot_token = os.environ["TG_BOT_TOKEN"]
    channel_id = os.environ["TG_CHANNEL_ID"]
    bot = telegram.Bot(token=bot_token)
    parser = argparse.ArgumentParser()
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
    photo_path = args.photo_path or random.choice(get_images_from_path())
    publish_photo_to_channel(bot, channel_id, photo_path)


if __name__ == "__main__":
    main()