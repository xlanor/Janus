# Janus

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0) [![Travis CI](https://api.travis-ci.org/xlanor/Janus.svg?branch=master)]()

Experimental telegram bot for CryptoSG

This bot is inspired by [roolbot](https://github.com/bvanrijn/rules-bot)

Thanks to [Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot).

This bot supports the movement of messages between the following channels
- Main
- Spam
- Lambo
- OTC
- Onboarding
- ICO

## Usage
<img src="/demo/janus_demo.gif" >

- This bot is written and designed to be used by CryptoSG's telegram group admins.

## Licensing
Janus is licensed under the AGPLv3. Looked at the LICENSE.md file for clarification.

## Expected Behavior
- Only responds to admins.
- Non admins trying to trigger comments will simply have the message wiped in the interest of reducing spam.
- The original message will not be deleted to provide some context.
- All trigger and exception messages in the main channel is to be wiped.
- The bot requires admin status in order to wipe trigger messages.
- GIF and Picture moving are supported
