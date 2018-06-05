import re


def is_sent_by_admin(message):
    user = message.chat.get_member(message.from_user.id)
    return user.status in ('administrator', 'creator')


def offtopic_forwarder(bot, update, off_topic_group_id):
    text = update.message.text
    if text.startswith('!offtopic') and update.message.reply_to_message and is_sent_by_admin(update.message):
        rematch = re.match('!offtopic ([0-9]+)+$', text)
        if rematch:
            for i in range(int(rematch.group(1)))[::-1]:
                bot.forward_message(
                    off_topic_group_id, update.message.chat_id,
                    update.message.reply_to_message.message_id - i
                )
        else:
            bot.forward_message(
                off_topic_group_id, update.message.chat_id,
                update.message.reply_to_message.message_id
            )
