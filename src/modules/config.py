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

	def get_bot_token(self):
		return self.token