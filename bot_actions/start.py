import logging

from telegram.ext import run_async


@run_async
def handler_start(bot, update, args):
    if update.effective_chat.type == "private":
        update.effective_message.reply_text("i will show help")
        # if len(args) >= 1:
        #     if args[0].lower() == "help":
        #         send_help(update.effective_chat.id, HELP_STRINGS)
        #
        #     elif args[0].lower().startswith("stngs_"):
        #         match = re.match("stngs_(.*)", args[0].lower())
        #         chat = dispatcher.bot.getChat(match.group(1))
        #
        #         if is_user_admin(chat, update.effective_user.id):
        #             send_settings(match.group(1), update.effective_user.id, False)
        #         else:
        #             send_settings(match.group(1), update.effective_user.id, True)
        #
        #     elif args[0][1:].isdigit() and "rules" in IMPORTED:
        #         IMPORTED["rules"].send_rules(update, args[0], from_pm=True)
        #
        # else:
        #     first_name = update.effective_user.first_name
        #     update.effective_message.reply_text(
        #         PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name), OWNER_ID),
        #         parse_mode=ParseMode.MARKDOWN)
    # else:
    # TODO: if not admin, then warn/mute user for abusing command
    # update.effective_message.reply_text("Please don't abusing bot commands")
