#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Janus read config
# Written by xlanor
##
import json
import os.path

class Configuration():
	def __init__(self):
		try:
			credentials_file = os.path.dirname(__file__) + '/../credentials.json'
			with open(credentials_file,'r',encoding='utf-8') as json_data:
				d = json.load(json_data)
		except FileNotFoundError:
			self.token = "-" #this will cause bot to error
		else:
			self.token = d["token"]
		try:
			chan_file = os.path.dirname(__file__) + '/../channels.json'
			with open(chan_file,'r',encoding='utf-8') as chan_json_data:
				chand = json.load(chan_json_data)
		except FileNotFoundError:
			self.error_chan = "-" #this will cause bot to error
		else:
			self.error_chan = chand["error_channel"]
		try:
			chan_file = os.path.dirname(__file__) + '/../channels.json'
			with open(chan_file,'r',encoding='utf-8') as chan_json_data:
				movabled = json.load(chan_json_data)
		except FileNotFoundError:
			self.movable_chan = "-" #this will cause bot to error
		else:
			self.spam_chan = chand["movable_channel"]["spam"]

	def get_bot_token(self):
		return self.token

	def error_channel(self):
		return self.error_chan

	def spam_channel(self):
		return self.spam_chan