#!/usr/bin/env python3

from bot import Bot
from decouple import config
import logging

if __name__ == '__main__':
    DEBUG = config("DEBUG", default=False, cast=bool)
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG if DEBUG else logging.INFO
    )
    token = config("TOKEN", cast=str)
    webhook_url = config('WEBHOOK_URL', cast=str)
    port = config('PORT', default=5000, cast=int)
    url = config('URL', default="127.0.0.1")
    workers = config('WORKERS', default=4, cast=int)
    private_key = config('PRIVATE_KEY', default=None)
    certificate = config('CERTIFICATE', default=None)

    logging.warning('Starting...')

    bot = Bot(
        token, url, webhook_url, port=port, workers=workers,
        private_key=private_key, certificate=certificate, debug=DEBUG
    )
    bot.run()
