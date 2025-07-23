from __future__ import annotations

import asyncio

from telethon import TelegramClient, events

from app.core.config import TELEGRAM_API_HASH, TELEGRAM_API_ID, TOKEN


async def main() -> None:
    print("Add your bot with privacy mode disabled as admin in your channel")
    print("Type `cid` in your channel to receive the channel id and configure the CID environment variable")

    client = TelegramClient("bot_setup", TELEGRAM_API_ID, TELEGRAM_API_HASH, bot_token=TOKEN)

    @client.on(events.NewMessage(pattern="cid"))
    async def cid_handler(event):
        chat_id = event.chat_id
        print(f"CID: {chat_id}")
        await event.reply(str(chat_id))

    async with client:
        await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
