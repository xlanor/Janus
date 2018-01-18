#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Janus commands
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
		self.approved = [#main channel here] 
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
						param = param.split()
						try:
							param[1]
						except IndexError:
							update.message.reply_text("You need to enter a parameter!",parse_mode='HTML')
						else:
							param = param[1].lower()
							if param in self.channels:
								self.move_to_channel(bot,update,param)
							else:
								self.parameters(bot,update)

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

	def move_to_channel(self,bot,update,type_of_ch):
		try:
			if type_of_ch == "spam":
				ch_id = Configuration().spam_channel()
				ch_name = Configuration().spam_channel_name()
				ch_url = Configuration().spam_channel_url()

			username = update.message.reply_to_message.from_user.username if update.message.reply_to_message.from_user.username else update.message.reply_to_message.from_user.first_name
			reply_to_message = update.message.reply_to_message.text 
			message = """This message was moved here from @CryptoSG \n\n"""
			message += """<i>@{0} wrote:\n {1}</i>\n\n """.format(username,reply_to_message)
			message += """⬇️ Please continue this discussion here! ⬇️"""

			sentmessage = bot.sendMessage(chat_id=ch_id,text=message,parse_mode='HTML')
			ch_url = ''.join([ch_url,"/", str(sentmessage.message_id)]) 
			main_message = "This message has been moved to {0}\n\n".format(ch_name)
			main_message += """➡️Please click <a href="{0}">here</a> to continue the conversation⬅️""".format(ch_url)
			update.message.reply_text(main_message,disable_web_page_preview=True,parse_mode='HTML',reply_to_message_id=update.message.reply_to_message.message_id)

		except Exception as e: 
			#while all encompassing exceptions are not good, we dont want to rr our bot each time.
			# we log and send to erro rch for debugging
			catcherror = traceback.format_exc()
			bot.sendMessage(chat_id=Configuration().error_channel(),text=catcherror,parse_mode='HTML')

	def parameters(self,bot,update):
		try:
			message = "These are a list of params that admins can use with /move\n\n"
			for param in self.channels:
				message += "- "
				message += param
				message += "\n"

			bot.sendMessage(chat_id=update.message.chat_id,text=message,parse_mode='HTML')

		except Exception as e: 
			#while all encompassing exceptions are not good, we dont want to rr our bot each time.
			# we log and send to erro rch for debugging
			catcherror = traceback.format_exc()
			bot.sendMessage(chat_id=Configuration().error_channel(),text=catcherror,parse_mode='HTML')

	### for debugging purpose only
	def get_raw_data(self,bot,update):
		print (update)