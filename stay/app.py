import asyncio
import os
import logging

from telethon import TelegramClient, events
from telethon.tl.functions import messages

from stay.configuration import EnvConfig

_log = logging.getLogger(__name__)


config = EnvConfig(os.environ.copy())


def create_client():
    client = TelegramClient('nevermind', config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)

    client.add_event_handler(on_user_left_group, events.ChatAction(config.TELEGRAM_TARGET_GROUP_ID))

    return client


async def on_user_left_group(event):
    if not event.user_left:
        return

    if not _is_target_user(event.user_id):
        return

    await asyncio.sleep(30)  # seconds

    await add_user_to_chat(event.client, event.user)


def _is_target_user(user_id):
    _log.debug('target user: %s', user_id)

    return user_id == config.TELEGRAM_TARGET_USER_ID


async def add_user_to_chat(client, user):
    await client(messages.AddChatUserRequest(
        chat_id=config.TELEGRAM_TARGET_GROUP_ID,
        user_id=user,
        fwd_limit=100,  # nevermind
    ))


async def main():
    client = create_client()

    async with client:
        await client.send_message('me', 'Hello, myself!')
        await client.run_until_disconnected()
