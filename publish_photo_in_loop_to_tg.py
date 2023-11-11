import os
import random
import time

import telegram
from dotenv import load_dotenv

from image_files_helpers import get_images_from_path

SECONDS_IN_MINUTE = 60


def main():
    load_dotenv()
    bot_token = os.environ["TG_BOT_TOKEN"]
    channel_id = os.environ["TG_CHANNEL_ID"]
    publish_frequency = int(os.getenv("PUBLISH_FREQUENCY_IN_MINUTES", 240))
    bot = telegram.Bot(token=bot_token)
    images_to_publish = get_images_from_path()
    random.shuffle(images_to_publish)
    while True:
        if not images_to_publish:
            images_to_publish = get_images_from_path()
            random.shuffle(images_to_publish)
        photo_path = images_to_publish.pop()
        bot.send_photo(chat_id=channel_id, photo=open(photo_path, "rb"))
        print(
            f"Successfully published {photo_path}"
            f" to the Telegram channel with ID {channel_id}."
        )
        print(f"Next post in {publish_frequency} minutes.")
        time.sleep(publish_frequency * SECONDS_IN_MINUTE)


if __name__ == "__main__":
    main()
