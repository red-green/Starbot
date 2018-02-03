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

from api import command, message, plugin, database
from api.bot import Bot
from api.database.table import Table, TableTypes
from libs import displayname


@Bot.client.event
async def on_member_join(member):
	# Welcome new user.
	await Bot.client.send_message(member.server, content = "Welcome " + member.mention + " to **" + member.server.name + "**!")

@Bot.client.event
async def on_member_remove(member):
	# Say goodbye to user.
	await Bot.client.send_message(member.server, content = "Goodbye *" + displayname.name(member) + "*, **" + member.server.name + "** will miss you!")


async def welcome_cmd(message_in):
	# Initialize database.
	database.init()
	table_greetings = Table("greetings", TableTypes.pServer)
	### NYI i guess


def onInit(plugin_in):
	commands_list = [
		command.Command(plugin_in, "setwelcome", welcome_cmd, shortdesc="Set the welcome message for the server [NYI].")
	]
	return plugin.Plugin(plugin_in, "greetings", commands_list)