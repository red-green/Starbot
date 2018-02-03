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
'''Get cache usage info'''

import glob
from api import command, message, plugin, bot

def cachecount_cmd(message_in):
	if message_in.body == '':
		return message.Message(body='No plugin specified')
	return message.Message(body='```{}```'.format(len(glob.glob('cache/{}_*'.format(message_in.body.strip())))))

def caches_cmd(message_in):
	cache_str = ''
	for cmd in bot.Bot.commands:
		cmd_cache_size = len(glob.glob('cache/{}_*'.format(cmd.name)))
		if cmd_cache_size > 0:
			cache_str += '{} - {}\n'.format(cmd.name, cmd_cache_size)
	return message.Message(body='```{}```'.format(cache_str))

def totalcache_cmd(message_in):
	return message.Message(body='```{}```'.format(len(glob.glob('cache/*'))))

def cachecont_cmd(message_in):
	cacheCount = glob.glob("cache/{}_*".format(message_in.content.split(' ')[-1]))
	cacheString = '\n'.join(cacheCount)
	return message.Message("```{}```".format(cacheString))


#####################

def init(plugin_in):
	commands_list = [
		command.Command(plugin_in, 'cachecount', cachecount_cmd, shortdesc='Count the number of cached items for a command', devcommand=True),
		command.Command(plugin_in, 'caches', caches_cmd, shortdesc='Count the number of cached items per command', devcommand=True),
		command.Command(plugin_in, 'totalcache', totalcache_cmd, shortdesc='Count the number of cached items stored', devcommand=True),
		command.Command(plugin_in, 'cachecontents', cachecont_cmd, shortdesc='List the content of the cache', devcommand=True)
	]
	this_plugin = plugin.Plugin(plugin_in, 'cacheutils', commands_list)
	return this_plugin

