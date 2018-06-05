import logging

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from bot_actions import handler_start, handler_error
from bot_actions.offtopic_forwarder import offtopic_forwarder


class Bot:
    off_topic_group_id = -1001119512908
    python_group_id = -1001050982793

    def __init__(self, token, url, webhook_url, private_key, certificate, port=8000, workers=4):
        self._webhook_url = webhook_url
        self._token = token
        self._url = url
        self._port = port
        self._private_key = private_key
        self._certificate = certificate
        self._updater = Updater(token, workers=workers)
        self._init_handlers()

    def run(self):
        u = self._updater
        u.start_webhook(
            listen=self._url,
            port=self._port,
            url_path=self._token,
            key=self._private_key,
            cert=self._certificate,
        )
        u.bot.set_webhook(
            '{}/{}'.format(
                self._webhook_url,
                self._token,
            )
        )
        logging.warning('Bot Running~')
        u.idle()

    def echo(self, bot, update):
        if update.message.chat_id not in (self.python_group_id, self.off_topic_group_id):
            update.effective_message.reply_text("thank you for inviting me here, but i must take my leave :)")
            bot.leave_chat(update.message.chat_id)
        else:
            offtopic_forwarder(bot, update, self.off_topic_group_id)

    def _init_handlers(self):
        start_handler = CommandHandler("start", handler_start, pass_args=True)

        dp = self._updater.dispatcher
        dp.add_handler(start_handler)
        dp.add_handler(MessageHandler(Filters.text, self.echo))
        dp.add_error_handler(handler_error)
