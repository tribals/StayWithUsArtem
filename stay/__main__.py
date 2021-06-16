import asyncio
import os

from stay.app import app
from stay.configuration import EnvConfig, TOMLFileConfig


def main():
    asyncio.run(app(EnvConfig(os.environ.copy()), None))


def winmain(config_path, code_callback):
    asyncio.run(app(TOMLFileConfig(config_path), code_callback))


if __name__ == '__main__':
    main()
