import io
from telethon import TelegramClient

from app.core.config import CID, TELEGRAM_API_HASH, TELEGRAM_API_ID, TOKEN
from app.storage.storage import Storage


class TelegramBotStorage(Storage):
    """A Telegram storage that operates through a bot token using Telethon."""

    def client(self) -> TelegramClient:
        return TelegramClient("bot", TELEGRAM_API_ID, TELEGRAM_API_HASH, bot_token=TOKEN)

    async def put_file(self, file: bytes, filename: str) -> str:
        buffer = io.BytesIO(file)
        buffer.name = filename
        async with self.client() as bot:
            message = await bot.send_file(int(CID), buffer, file_name=filename)
            return str(message.id)

    async def get_file(self, file_id: str):
        async with self.client() as bot:
            message = await bot.get_messages(int(CID), ids=int(file_id))
            buffer = io.BytesIO()
            await bot.download_media(message, file=buffer)
            buffer.seek(0)
            return buffer
