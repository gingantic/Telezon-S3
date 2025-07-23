from app.storage.storage import Storage
from app.storage.telegram import (  # noqa: F401
    TelegramAccountStorage,
    TelegramBotStorage,
)

# You can use TelegramBotStorage or TelegramAccountStorage
# TelegramBotStorage uses Telethon with a bot token (Bot API)
# TelegramAccountStorage uses Telethon with a user session (MTProto)
storage: Storage = TelegramAccountStorage()
