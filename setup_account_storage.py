from __future__ import annotations

import asyncio
import os

from telethon import TelegramClient, events
from telethon.sessions import StringSession

from app.core.config import TELEGRAM_API_HASH, TELEGRAM_API_ID


async def main() -> None:
    session_string = os.getenv("SESSION_STRING", "")

    if session_string:
        client = TelegramClient(StringSession(session_string), TELEGRAM_API_ID, TELEGRAM_API_HASH)
    else:
        client = TelegramClient("setup", TELEGRAM_API_ID, TELEGRAM_API_HASH)

    async with client:
        # If we didn't have a session, print it so the user can store it
        if not session_string:
            print("Save this in SESSION_STRING environment variable\n")
            print(client.session.save())
            print("\n")

        @client.on(events.NewMessage)
        async def cid_handler(event):
            print(f"CHANNEL ID {event.chat_id}")

        print(
            "Send a message in your channel and copy the printed CHANNEL ID to the CID environment variable"
        )
        print("PRESS Ctrl^c to stop")
        await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
