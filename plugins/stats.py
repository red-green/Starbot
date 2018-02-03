#    Copyright 2018 Starbot Discord Project
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
'''Get cache usage info'''

from api import command, message, plugin
from api.bot import Bot

def messages_cmd(message_in):
	# Get server.
	server = message_in.server

	# If the server is null, show error.
	if not server:
		return message.Message("This is not a server. :wink:")

	msg_count = Bot.messagesSinceStart
	msg_count_server = logging.message_count_get(server.id)
	msg = "I've witnessed *{} messages* since I started and *{} messages* overall!"
	return message.Message(msg.format(msg_count, msg_count_server))

def message_cb(message_in, is_command):
	# this will get called with every message that the bot recieves, and in this case, is tracking statistics
	if message_in.server and not is_command:
		logging.message_log(message_in, message_in.server.id)
		count = logging.message_count_get(message_in.server.id)
		Bot.messagesSinceStart += 1
		count += 1


#####################

def init(plugin_in):
	commands_list = [
		command.Command(plugin_in, 'messages', messages_cmd, shortdesc="Show how many messages the bot has seen since start"),
	]
	this_plugin = plugin.Plugin(plugin_in, 'cacheutils', commands_list, callback=message_cb)
	return this_plugin

