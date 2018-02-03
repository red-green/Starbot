#    Copyright 2017 Starbot Discord Project
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import importlib
import time
import sys
import asyncio

import discord
from pluginbase import PluginBase

from api import settings, message, logging, commandmanager
from api import command as command_api
from api.bot import Bot
from libs import displayname
from api import database


class FakeClient: # what is this for?
	def event(self):
		pass

if __name__ == "__main__":
	database.init()

	# Log the time we started.
	Bot.startTime = time.time()

	# Create the Discord client.
	client = discord.Client()
	Bot.client = client

	commandmanager.load_all_plugins()

	# Get our token to use.
	token = ""
	with open("token.txt") as m:
		token = m.read().strip()
else:
	client = discord.Client()
	Bot.client = client


@client.event
async def on_ready():
	# Print logged in message to console.
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------")
	print("Bot Invite Link: " + "https://discordapp.com/oauth2/authorize?client_id=" + client.user.id + "&scope=bot&permissions=8")
	print("------")

	# Set the game.
	await client.change_presence(game=discord.Game(name="with magic"))


@client.event
async def on_message(message_in):
	# Ignore messages that aren't from a server and from ourself.
	#if not message_in.server:
	 #   return
	if message_in.author.id == client.user.id:
		return
	if message_in.author.bot:
		return

	# Send typing message.
	await client.send_typing(message_in.channel)

	# Build message object.
	message_recv = message.Message
	message_recv.command = command.name
	if message_in.content.startswith("{} ".format(me.mention)):
		message_recv.body = message_in.content.split("{} ".format(me.mention) + command.name, 1)[1]
	else:
		message_recv.body = message_in.content.split(prefix + command.name, 1)[1]
	message_recv.author = message_in.author
	message_recv.server = message_in.server
	message_recv.mentions = message_in.mentions
	message_recv.channel = message_in.channel

	resp = await commandmanager.parse_command(message_recv)
	is_command = resp != None

	if type(command_result) is list and len(command_result) > 5:  # PM messages.
		# Send message saying that we are PMing the messages.
		await client.send_message(message_in.channel, "Because the output of that command is **{} pages** long, I'm just going to PM the result to you.".format(len(command_result)))

		# PM it.
		for item in command_result:
			await process_message(message_in.author, message_in, item)

	else: # Send to channel.
		for item in command_result:
			await process_message(message_in.channel, message_in, item)

	# Do regular message.
	else:
		await process_message(message_in.channel, message_in, command_result)

		# Do we delete the message afterwards?
		if message_in.server and command_result.delete:
			await client.delete_message(message_in)


async def process_message(target, message_in, msg):
	# If the message to send has a body
	if msg.body:
		# Remove @everyone and @here from messages.
		zerospace = "​"
		msg.body = msg.body.replace("@everyone", "@{}everyone".format(zerospace)).replace("@here", "@{}here".format(zerospace))

	# If the message to send includes a file
	if msg.file != "":
		# Send the file, along with any possible message
		await client.send_file(target, msg.file, content=msg.body)
	else:
		# Send the message, along with a possible embed
		await client.send_message(target, msg.body, embed=msg.embed)

if __name__ == "__main__":
	# Start bot.
	# THIS MUST ALWAYS BE DOWN HERE
	# I found this out after 3 days of stupidity and tried filing a report with the Discord.py devs to figure out why the
	# library seems to have hanged when it was in the initial block of the same if. I still don't know. They disregarded
	# the entirety of my ticket and told me that this is a blocking call. Yeah, I know. But if you read the rest of the ticket
	# you would know that after this function was called all the main thread would drop and the bot would become unresponsive.
	# But apparently it is the debugger I explicitly stated that I had turned off on some of my messages I sent while figuring it out.
	# I don't know why you would lock a ticket because of a debugger that isn't on and a problem you were ignoring.
	# Maybe someone should add a warning to the Discord.py library for when you run client.run in the wrong place.
	# But honestly I can't be bothered.
	client.run(token)
