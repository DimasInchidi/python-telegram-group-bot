from bot import Bot
from decouple import config
import logging

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    token = config("TOKEN")
    webhook_url = config('WEBHOOK_URL')
    port = config('PORT', default=5000, cast=int)
    url = config('URL', default="127.0.0.1")
    workers = config('WORKERS', default=4, cast=int)
    private_key = config('PRIVATE_KEY', default=None, cast=str)
    certificate = config('CERTIFICATE', default=None, cast=str)

    logging.warning('Starting...')

    bot = Bot(
        token, url, webhook_url, port=port, workers=workers,
        private_key=private_key, certificate=certificate
    )
    bot.run()
