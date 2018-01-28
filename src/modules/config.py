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
			self.spam_chan = "-" #this will cause bot to error
			self.spam_chan_name = "-"
			self.spam_chan_url = "-"
			self.otc_chan =  "-"
			self.otc_chan_name = "-"
			self.otc_chan_url = "-"
		else:
			self.spam_chan = chand["movable_channel"]["spam"]["id"]
			self.spam_chan_name = chand["movable_channel"]["spam"]["name"]
			self.spam_chan_url = chand["movable_channel"]["spam"]["url"]
			self.otc_chan = chand["movable_channel"]["otc"]["id"]
			self.otc_chan_name = chand["movable_channel"]["otc"]["name"]
			self.otc_chan_url = chand["movable_channel"]["otc"]["url"]
			self.onboarding_chan = chand["movable_channel"]["onboarding"]["id"]
			self.onboarding_chan_name = chand["movable_channel"]["onboarding"]["name"]
			self.onboarding_chan_url = chand["movable_channel"]["onboarding"]["url"]
			self.lambo_chan = chand["movable_channel"]["lambo"]["id"]
			self.lambo_chan_name = chand["movable_channel"]["lambo"]["name"]
			self.lambo_chan_url = chand["movable_channel"]["lambo"]["url"]
			self.ico_chan = chand["movable_channel"]["ico"]["id"]
			self.ico_chan_name = chand["movable_channel"]["ico"]["name"]
			self.ico_chan_url = chand["movable_channel"]["ico"]["url"]
			self.main_chan = chand["movable_channel"]["main"]["id"]
			self.main_chan_name = chand["movable_channel"]["main"]["name"]
			self.main_chan_url = chand["movable_channel"]["main"]["url"]
			approved_channel = []
			for chan,val in chand["movable_channel"].items():
				try:
					chid = int(val['id'])
					approved_channel.append(chid)
				except ValueError:
					pass #for our dummy vals

			self.approved_ch = approved_channel

	def get_bot_token(self):
		return self.token

	def error_channel(self):
		return self.error_chan

	def spam_channel(self):
		return self.spam_chan

	def spam_channel_name(self):
		return self.spam_chan_name

	def spam_channel_url(self):
		return self.spam_chan_url

	def otc_channel(self):
		return self.otc_chan

	def otc_channel_name(self):
		return self.otc_chan_name

	def otc_channel_url(self):
		return self.otc_chan_url

	def onboarding_channel(self):
		return self.onboarding_chan

	def onboarding_channel_name(self):
		return self.onboarding_chan_name

	def onboarding_channel_url(self):
		return self.onboarding_chan_url

	def lambo_channel(self):
		return self.lambo_chan

	def lambo_channel_name(self):
		return self.lambo_chan_name

	def lambo_channel_url(self):
		return self.lambo_chan_url
		
	def ico_channel(self):
		return self.ico_chan

	def ico_channel_name(self):
		return self.ico_chan_name

	def ico_channel_url(self):
		return self.ico_chan_url

	def main_channel(self):
		return self.main_chan

	def main_channel_name(self):
		return self.main_chan_name

	def main_channel_url(self):
		return self.main_chan_url

	def get_all_approved_channels(self):
		return self.approved_ch