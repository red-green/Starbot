from api import message
from api.bot import Bot

async def run(message_in):
    plugin_list = []
    for plugin_in in Bot.plugins:
        plugin_list.append(plugin_in.name)
    return message.Message(body='```{}```'.format(', '.join(plugin_list)))