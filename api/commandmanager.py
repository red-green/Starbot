# todo: insert the header thingy


# all the magic happens here; indexing for commands and (hopefully) more efficient lookup


from bot import Bot
import settings
from command import is_command
from pluginbase import PluginBase

command_map = {}
callbacks = []


def load_plugin(plugin_source, plugin, autoimport=True):
	global command_map, callbacks

	if autoimport == True:
		plugin_temp = plugin_source.load_plugin(plugin)
		plugin_info = plugin_temp.init(plugin_temp)
	else:
		plugin_info = plugin.init(plugin)

	if plugin_info.callback:
		callbacks.append(plugin_info.callback)

	# Verify the plugin is defined, it has a name, and it has commands.
	if plugin_info.plugin == None:
		print("Plugin not defined!")
	if plugin_info.name == None:
		print("Plugin name not defined")
	if plugin_info.commands == []:
		print("Plugin did not define any commands.")
	for command in plugin_info.commands: # Verify each command has a parent plugin and a name.
		if command.plugin == None:
			print("Plugin command does not define parent plugin")
		if command.name == None:
			print("Plugin command does not define name")

	# Add plugin to list.
	Bot.plugins.append(plugin_info)

	for command in plugin_info.commands:
		# Add command to list of commands and print a success message.
		Bot.commands.append(command)
		for alias in command.all_commands:
			command_map[alias] = command # save this in a hashmap for lookup later
		print("Command `{}` registered successfully.".format(command.name))

	# Print success message.
	print("Plugin '{}' registered successfully.".format(plugin_info.name))


def load_all_plugins():
	plugin_base = PluginBase(package="plugins")
	plugin_source = plugin_base.make_plugin_source(searchpath=["./plugins"])

	for plugin in plugin_source.list_plugins():
		load_plugin(plugin_source,plugin)


def parse_command(message_in):

	if message_in.server:
		prefix = settings.prefix_get(message_in.server.id)
		me = message_in.server.me
	else:
		prefix = ''
		me = message_in.channel.me

	message_split = message_in.content.strip().split()

	cmd_string = ''
	cmd_class = None
	args = []
	has_cmd = False

	if len(message_split) >= 1 and message_split[0].startswith(prefix):
		cmd_string = message_split[0].replace(prefix,'',1)
		if len(message_split) > 1:
			args = message_split[1:]
		has_cmd = True

	elif len(message_split) >= 2 and message_split[0] == me.mention:
		cmd_string = message_split[1]
		if len(message_split) > 2:
			args = message_split[2:]
		has_cmd = True

	if has_cmd:
		cmd_class = command_map.get(cmd_string,None)
		if not cmd_class:
			has_cmd = False

	for cb_func in callbacks:
		cb_func(message_in, has_cmd)

	if has_cmd:
		message_in.args = cmd_args
		return cmd_class.function(message_in)
	else:
		return None
