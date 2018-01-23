#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Janus commands
# Written by xlanor
##
import traceback
import json
from telegram import ReplyKeyboardMarkup,ChatAction,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Job , ConversationHandler
from contextlib import closing
from modules.config import Configuration

class Commands():
	def __init__(self):
		self.approved = ["-"]
		self.channels = ["spam","otc","lambo","onboarding","ico"]

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

	def handle_message(self,bot,update,job_queue):
		try:
			print (update)
			user_sent_message = update.message.message_id
			admin_list = self.get_admins_list(bot,update)
			if update.message.chat_id in self.approved:
				try:
					replied_message = update.message.reply_to_message.message_id
				except AttributeError:
					message = "You need to select a message to move!"
					nomsg = update.message.reply_text(message,parse_mode='HTML')
					context = [update.message.chat_id,nomsg.message_id]
					job_queue.run_once(self.delete_message_queue, 10, context= context, name="Delete params")
				else:
					if update.message.from_user.id in admin_list:
						param = update.message.text
						param = param.split()
						try:
							param[1]
						except IndexError:
							indexmsg = update.message.reply_text("You need to enter a parameter!",parse_mode='HTML')
							context = [update.message.chat_id,indexmsg.message_id]
							job_queue.run_once(self.delete_message_queue, 10, context= context, name="Delete params")

						else:
							param = param[1].lower()
							if param in self.channels:
								self.move_to_channel(bot,update,param)
							else:
								self.parameters(bot,update,job_queue)
								
				context = [update.message.chat_id,user_sent_message]
				job_queue.run_once(self.delete_message_queue, 10, context= context, name="Delete params")
			else
				if update.message.from_user.id in admin_list:
					wrongch = update.message.reply_text("This bot can only be used to move messages in CryptoSG!",parse_mode='HTMl')

					context = [update.message.chat_id,wrongch.message_id]
					job_queue.run_once(self.delete_message_queue, 10, context= context, name="Delete params")

					context = [update.message.chat_id,user_sent_message]
					job_queue.run_once(self.delete_message_queue, 10, context= context, name="Delete params")
			

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

			elif type_of_ch == "otc":
				ch_id = Configuration().otc_channel()
				ch_name = Configuration().otc_channel_name()
				ch_url = Configuration().otc_channel_url()

			elif type_of_ch == "lambo":
				ch_id = Configuration().lambo_channel()
				ch_name = Configuration().lambo_channel_name()
				ch_url = Configuration().lambo_channel_url()

			elif type_of_ch == "onboarding":
				ch_id = Configuration().onboarding_channel()
				ch_name = Configuration().onboarding_channel_name()
				ch_url = Configuration().onboarding_channel_url()

			elif type_of_ch == "ico":
				ch_id = Configuration().ico_channel()
				ch_name = Configuration().ico_channel_name()
				ch_url = Configuration().ico_channel_url()

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

	def parameters(self,bot,update,job_queue):
		try:
			message = "These are a list of params that admins can use with /move\n\n"
			for param in self.channels:
				message += "- "
				message += param
				message += "\n"

			parammsg = bot.sendMessage(chat_id=update.message.chat_id,text=message,parse_mode='HTML')

			context = [update.message.chat_id,parammsg.message_id]
			job_queue.run_once(self.delete_message_queue, 10, context= context, name="Delete params")

		except Exception as e: 
			#while all encompassing exceptions are not good, we dont want to rr our bot each time.
			# we log and send to erro rch for debugging
			catcherror = traceback.format_exc()
			bot.sendMessage(chat_id=Configuration().error_channel(),text=catcherror,parse_mode='HTML')


	def delete_message_queue(self,bot,job):
		try:
			bot.delete_message(chat_id = job.context[0],message_id = job.context[1])

		except Exception as e: 
			#while all encompassing exceptions are not good, we dont want to rr our bot each time.
			# we log and send to erro rch for debugging
			catcherror = traceback.format_exc()
			bot.sendMessage(chat_id=Configuration().error_channel(),text=catcherror,parse_mode='HTML')

	### for debugging purpose only
	def get_raw_data(self,bot,update):
		print (update)
