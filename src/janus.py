#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Janus init
# Written by xlanor
##

import telegram
from commands import Commands
from modules.config import Configuration
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,Job, MessageHandler, Filters, RegexHandler, ConversationHandler

def test():
	updater = Updater(token=Configuration().get_bot_token())
	dispatcher = updater.dispatcher
	handle_message_handler = CommandHandler('move', Commands().handle_message)
	dispatcher.add_handler(handle_message_handler)
	print("Janus online")
	updater.start_polling()
	updater.idle

if __name__ == "__main__":
	test()