from api import command, plugin, message
from plugins.search import google
import urllib

# Search plugin
def onInit(plugin_in):
    google_command = command.Command(plugin_in, 'google', shortdesc='Google it!', customfunction=google.search)
    bing_command = command.Command(plugin_in, 'bing', shortdesc='Uhh... Bing it?')
    duckduckgo_command = command.Command(plugin_in, 'duckduckgo', shortdesc='Ask the duck.')
    aol_command = command.Command(plugin_in, 'aol', shortdesc='Here you go, gramps')
    return plugin.Plugin(plugin_in, 'search', [google_command, bing_command, duckduckgo_command, aol_command])

async def onCommand(message_in):
    return