from api import message
from api.bot import Bot

def commands_detect_dups():
    duplicates = []
    commands_list = []
    for plugin_in in Bot.plugins:
        for command_in in plugin_in.commands:
            commands_list.append(command_in.name)

    for command_in in commands_list:
        commandOccurances = 0
        for command2 in commands_list:
            if command_in == command2:
                commandOccurances += 1
        if commandOccurances > 1:
            duplicates.append(command_in)

    return list(set(duplicates))

async def run(message_in):
    dups = commands_detect_dups()
    plugin_string = '```\n'
    for plugin_in in Bot.plugins:
        plugin_string += '{}\n'.format(plugin_in.name)
        plugin_commands = len(plugin_in.commands)
        index = 0
        for command_in in plugin_in.commands:
            index += 1
            if plugin_commands != index:
                if command_in.name in dups:
                    plugin_string += '├ {} <-- duplicate\n'.format(command_in.name)
                else:
                    plugin_string += '├ {}\n'.format(command_in.name)
            else:
                if command_in.name in dups:
                	plugin_string += '└ {} <-- duplicate\n'.format(command_in.name)
                else:
                    plugin_string += '└ {}\n'.format(command_in.name)
    plugin_string += '```'
    return message.Message(body=plugin_string)