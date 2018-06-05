import logging
from .start import handler_start


def handler_error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))
