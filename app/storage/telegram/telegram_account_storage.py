import io
from telethon import TelegramClient
from telethon.sessions import StringSession

from app.core.config import CID, SESSION_STRING, TELEGRAM_API_HASH, TELEGRAM_API_ID
from app.storage.storage import Storage


class TelegramAccountStorage(Storage):
    """
    Store and retrieve objects in a private Telegram channel **using a user account**
    authorised with Telethon.
    """

    def client(self) -> TelegramClient:
        """Return an unauthorised `TelegramClient` instance."""
        return TelegramClient(StringSession(SESSION_STRING), TELEGRAM_API_ID, TELEGRAM_API_HASH)

    async def put_file(self, file: bytes, filename: str) -> str:
        """Upload `file` as `filename` to the channel.

        Returns the **message id** under which the document was stored so that it can
        be downloaded later with `get_file`.
        """
        document = io.BytesIO(file)
        document.name = filename

        async with self.client() as client:
            message = await client.send_file(int(CID), document, file_name=filename)
            return str(message.id)

    async def get_file(self, file_id: str) -> io.BufferedReader:
        """Download the document previously stored under `file_id`."""
        async with self.client() as client:
            message = await client.get_messages(int(CID), ids=int(file_id))
            buffer = io.BytesIO()
            await client.download_media(message, file=buffer)
            buffer.seek(0)
            return buffer
