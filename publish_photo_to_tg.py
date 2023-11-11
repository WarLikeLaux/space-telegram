import argparse
import os
import random

import telegram
from dotenv import load_dotenv

from image_files_helpers import get_images_from_path


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
    bot.send_photo(chat_id=channel_id, photo=open(photo_path, "rb"))
    print(
        f"Successfully published {photo_path}"
        f" to the Telegram channel with ID {channel_id}."
    )


if __name__ == "__main__":
    main()
