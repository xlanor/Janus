#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Janus init
# Written by xlanor
##
import traceback
import json
from telegram import ReplyKeyboardMarkup,ChatAction,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,Job,ConversationHandler
from contextlib import closing
from modules.config import Configuration

class Commands():
	def __init__(self):
		self.approved = [-1001186117544]
		self.channels = ["spam"]

	def get_admins_list(self,bot,update):
		try:
			admin_object_list = bot.getChatAdministrators(update.message.chat_id)
			admin_id_list = []
			for admin in admin_object_list:
				admin_id_list.append(admin.user.id)
			
			return admin_id_list

		except Exception as e: 
			#while all encompassing exceptions are not good, we dont want to rr our bot each time.
			# we log and send to erro rch for debugging
			catcherror = traceback.format_exc()
			bot.sendMessage(chat_id=Configuration().error_channel(),text=catcherror,parse_mode='HTML')

	def handle_message(self,bot,update):
		try:
			print(update)
			if update.message.chat_id in self.approved:
				try:
					replied_message = update.message.reply_to_message.message_id
				except AttributeError:
					message = "You need to select a message to move!"
					update.message.reply_text(message,parse_mode='HTML')
				else:
					admin_list = self.get_admins_list(bot,update)
					if update.message.from_user.id in admin_list:
						param = update.message.text
						param = param.split(" ")
						try:
							param[1]
						except IndexError:
							update.message.reply_text("You need to enter a parameter!",parse_mode='HTML')
						else:
							param = param[1]
							update.message.reply_text(param,parse_mode='HTML')

					else:
						message = "You aren't an administrator in this group!"
						update.message.reply_text(message,parse_mode='HTML')

			else:
				update.message.reply_text("This bot can only be used to move messages in CryptoSG!",parse_mode='HTMl')
			

		except Exception as e: 
			#while all encompassing exceptions are not good, we dont want to rr our bot each time.
			# we log and send to erro rch for debugging
			catcherror = traceback.format_exc()
			bot.sendMessage(chat_id=Configuration().error_channel(),text=catcherror,parse_mode='HTML')