import re

from telegram import Message, TelegramError

from utils.chat_member_status import can_delete, can_restrict_members


def is_sent_by_admin(message):
    user = message.chat.get_member(message.from_user.id)
    return user.status in ('administrator', 'creator')


def offtopic_forwarder(bot, update, python_off_topic_group_id, bot_sandbox_group):
    text = update.message.text
    is_bot_can_delete = can_delete(update.message.chat, bot.get_me().id)
    # is_bot_can_restrict_members = can_restrict_members(update.message.chat, bot.get_me().id)
    if text.startswith('!offtopic') and update.message.reply_to_message and is_sent_by_admin(update.message):
        rematch = re.match('!offtopic ([0-9]+)+$', text)
        if rematch:
            count_to_forward = int(rematch.group(1))
            start_message_id = update.message.reply_to_message.message_id
            message_ids = [start_message_id]
            n = 1
            while count_to_forward > 1 and n < 30:
                try:
                    bot.forward_message(
                        bot_sandbox_group, update.message.chat_id,
                        start_message_id - n
                    )
                    count_to_forward -= 1
                    message_ids.append(start_message_id - n)
                except TelegramError:
                    pass
                n += 1
            for i in message_ids[::-1]:
                bot.forward_message(
                    python_off_topic_group_id, update.message.chat_id,
                    i
                )
                if is_bot_can_delete:
                    bot.delete_message(update.message.chat_id, i)
                # if is_bot_can_restrict_members:
                #     bot.restrict_chat_member(update.message.chat_id, user_id, duration)
        else:
            bot.forward_message(
                python_off_topic_group_id, update.message.chat_id,
                update.message.reply_to_message.message_id
            )
