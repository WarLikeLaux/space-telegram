def publish_text_to_channel(bot, channel_id, text):
    bot.send_message(chat_id=channel_id, text=text)


def publish_photo_to_channel(bot, channel_id, photo_path):
    bot.send_photo(chat_id=channel_id, photo=open(photo_path, "rb"))


def main():
    pass


if __name__ == "__main__":
    main()
