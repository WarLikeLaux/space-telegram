import os
import random
import time

import telegram
from dotenv import load_dotenv

from image_files_helpers import get_images_from_path
from tg_helpers import publish_photo_to_channel

SECONDS_IN_MINUTE = 3


def main():
    load_dotenv()
    bot_token = os.environ["TG_BOT_TOKEN"]
    channel_id = os.environ["TG_CHANNEL_ID"]
    publish_frequency = int(os.environ["PUBLISH_FREQUENCY_IN_MINUTES"] or 240) 
    bot = telegram.Bot(token=bot_token)
    images_to_publish = get_images_from_path()
    random.shuffle(images_to_publish)
    while True:
        if not images_to_publish:
            images_to_publish = get_images_from_path()
            random.shuffle(images_to_publish)
        photo_path = images_to_publish.pop()
        publish_photo_to_channel(bot, channel_id, photo_path)
        time.sleep(publish_frequency * SECONDS_IN_MINUTE)


if __name__ == "__main__":
    main()
