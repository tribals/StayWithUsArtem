import asyncio
import logging

from telethon import TelegramClient, events
from telethon.tl.functions import messages

_log = logging.getLogger(__name__)


def create_client(config):
    client = TelegramClient('nevermind', config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)

    client.add_event_handler(on_user_left_group, events.ChatAction(config.TELEGRAM_TARGET_GROUP_ID))

    return client


async def on_user_left_group(event):
    if not event.user_left:
        return

    if not _is_target_user(event.user_id, event.client.config):
        return

    await asyncio.sleep(30)  # seconds

    await add_user_to_chat(event.client, event.user, event.client.config)


def _is_target_user(user_id, config):
    return user_id == config.TELEGRAM_TARGET_USER_ID


async def add_user_to_chat(client, user, config):
    await client(messages.AddChatUserRequest(
        chat_id=config.TELEGRAM_TARGET_GROUP_ID,
        user_id=user,
        fwd_limit=100,  # nevermind
    ))


async def app(config, code_callback):
    client = create_client(config)
    client.config = config  # HACK

    await client.start(config.TELEGRAM_PHONE, code_callback=code_callback)
    await client.run_until_disconnected()
