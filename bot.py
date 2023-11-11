import os

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    tg_channel_id = os.environ["TG_CHANNEL_ID"]
    bot = telegram.Bot(token=tg_bot_token)
    # bot.send_message(
    #     chat_id=tg_channel_id,
    #     text="I'm sorry Dave I'm afraid I can't do that."
    # )
    bot.send_photo(
        chat_id=tg_channel_id,
        photo=open('images/nasa_epic_0.png', 'rb')
    )


if __name__ == "__main__":
    main()
